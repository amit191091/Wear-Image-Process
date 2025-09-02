#!/usr/bin/env python3
"""
Data Utilities Module
============================

Data handling and file utilities for all analysis types:
- all_teeth: Full gear analysis data utilities
- tooth1: Single tooth analysis data utilities
"""

import sys
import os
import csv
from typing import List, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import get_config

def extract_wear_number(filename):
    """
    Extract wear case number from filename
    
    Args:
        filename: Image filename (e.g., "W1 scale 250.7 micro meter.jpg")
        
    Returns:
        int: Wear case number (e.g., 1)
    """
    basename = os.path.basename(filename)
    wear_match = basename.split(' ')[0]
    return int(wear_match[1:])

def enforce_monotonicity(results: List[Dict], analysis_type: str = "all_teeth") -> List[Dict]:
    """
    Enforce monotonicity in wear depth across wear cases
    
    Args:
        results: List of result dictionaries
        analysis_type: "all_teeth" or "tooth1"
        
    Returns:
        List[Dict]: Results with enforced monotonicity
    """
    if not results:
        return results
    
    if analysis_type == "all_teeth":
        return enforce_monotonicity_for_all_teeth(results)
    elif analysis_type == "tooth1":
        return enforce_monotonicity_for_tooth1(results)
    else:
        print(f"❌ Unknown analysis type: {analysis_type}")
        return results

def enforce_monotonicity_for_all_teeth(results: List[Dict]) -> List[Dict]:
    """
    Enforce monotonicity in wear depth across wear cases for all teeth
    """
    if not results:
        return results
    
    # Group by tooth number
    teeth_data = {}
    for result in results:
        tooth_num = result["tooth_number"]
        if tooth_num not in teeth_data:
            teeth_data[tooth_num] = []
        teeth_data[tooth_num].append(result)
    
    # Sort each tooth's data by wear case
    for tooth_num in teeth_data:
        teeth_data[tooth_num].sort(key=lambda x: x["wear_case"])
    
    # Enforce monotonicity for each tooth
    for tooth_num, tooth_results in teeth_data.items():
        max_wear = 0.0
        for result in tooth_results:
            current_wear = result["wear_depth_um"]
            if current_wear < max_wear:
                result["wear_depth_um"] = max_wear
            else:
                max_wear = current_wear
    
    return results

def enforce_monotonicity_for_tooth1(results: List[Dict]) -> List[Dict]:
    """
    Enforce monotonicity for tooth 1 analysis results
    """
    if not results:
        return results
    
    # Get configuration for max wear limit
    tooth1_config = get_config("tooth1")
    MAX_THEORETICAL_WEAR = tooth1_config.MAX_THEORETICAL_WEAR
    
    sorted_results = sorted(results, key=lambda x: x["wear_case"])
    
    for i in range(1, len(sorted_results)):
        current_wear = sorted_results[i]["wear_depth_um"]
        previous_wear = sorted_results[i-1]["wear_depth_um"]
        
        current_wear = max(0, current_wear)
        previous_wear = max(0, previous_wear)
        
        if current_wear < previous_wear:
            adjusted_wear = previous_wear * 1.02
            adjusted_wear = min(adjusted_wear, MAX_THEORETICAL_WEAR)
            adjusted_wear = max(0, adjusted_wear)
            
            sorted_results[i]["wear_depth_um"] = adjusted_wear
            # Add monotonic flag to method if it exists
            if "method" in sorted_results[i]:
                sorted_results[i]["method"] = sorted_results[i]["method"] + "_monotonic"
    
    return sorted_results

def save_results_to_csv(results, filename=None, analysis_type="all_teeth"):
    """
    Save results to CSV file based on analysis type
    
    Args:
        results: List of result dictionaries
        filename: Output filename (optional, will use default based on type)
        analysis_type: "all_teeth" or "tooth1"
    """
    if not results:
        print("❌ No results to save")
        return
    
    # Set default filename based on analysis type
    if filename is None:
        # Use current directory
        if analysis_type == "tooth1":
            filename = "single_tooth_results.csv"
        else:
            filename = "all_teeth_results.csv"
    
    # Save ONLY the table format (reshaped)
    save_table_format(results, filename, analysis_type)

def save_table_format(results, original_filename, analysis_type="all_teeth"):
    """
    Save results in table format with tooth numbers as rows and wear cases as columns
    
    Args:
        results: List of result dictionaries
        original_filename: Original CSV filename to derive table filename from
        analysis_type: "all_teeth" or "tooth1"
    """
    try:
        import pandas as pd
        
        # Convert to DataFrame
        df = pd.DataFrame(results)
        
        if analysis_type == "all_teeth" and "tooth_number" in results[0]:
            # All teeth results - pivot by tooth number
            # Pivot the data to create the table format
            # Rows: tooth_number, Columns: wear_case, Values: wear_depth_um
            table_df = df.pivot(index='tooth_number', columns='wear_case', values='wear_depth_um')
            
            # Reset index to make tooth_number a regular column
            table_df = table_df.reset_index()
            
            # Rename the index column to 'Tooth'
            table_df = table_df.rename(columns={'tooth_number': 'Tooth'})
            
            # Rename wear case columns to be more descriptive (W1, W2, etc.)
            wear_case_columns = {col: f'W{col}' for col in table_df.columns if col != 'Tooth'}
            table_df = table_df.rename(columns=wear_case_columns)
            
            # Round all numeric columns to 1 decimal place
            numeric_columns = [col for col in table_df.columns if col != 'Tooth']
            table_df[numeric_columns] = table_df[numeric_columns].round(1)
            
            # Sort by tooth number
            table_df = table_df.sort_values('Tooth')
            
            print(f"📊 Table shape: {table_df.shape} (rows: teeth, columns: wear cases)")
            
        else:
            # Single tooth results - create simple table with wear cases as columns
            # Create a single row with wear cases as columns
            wear_cases = sorted([result['wear_case'] for result in results])
            wear_depths = [next(r['wear_depth_um'] for r in results if r['wear_case'] == case) for case in wear_cases]
            
            # Create DataFrame with single row
            table_df = pd.DataFrame([wear_depths], columns=[f'W{case}' for case in wear_cases])
            
            # Round all numeric columns to 1 decimal place
            table_df = table_df.round(1)
            
            print(f"📊 Table shape: {table_df.shape} (single row, {len(wear_cases)} wear cases)")
        
        # Save the table format directly to the main filename
        table_df.to_csv(original_filename, index=False)
        
        print(f"✅ Results saved in table format to '{original_filename}'")
        
        return table_df
        
    except Exception as e:
        print(f"⚠️ Warning: Could not save table format: {str(e)}")
        return None

# Backward compatibility functions
def enforce_monotonicity_for_all_teeth_legacy(results: List[Dict]) -> List[Dict]:
    """Legacy function for backward compatibility"""
    return enforce_monotonicity_for_all_teeth(results)

def save_tooth1_results_to_csv(results):
    """Legacy function for backward compatibility with tooth1 analysis"""
    # Get the Picture directory path (parent of Picture Tools)
    picture_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(picture_dir, "single_tooth_results.csv")
    return save_results_to_csv(results, filename=filename, analysis_type="tooth1")