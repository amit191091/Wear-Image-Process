#!/usr/bin/env python3
"""
Main Orchestrator for Tooth 1 Analysis
======================================

Main function to run tooth 1 wear analysis using modular components
"""

import sys
import os
import traceback
import warnings
warnings.filterwarnings('ignore')

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from config import get_config
    from tooth1_analyzer import *
    from data_utils import save_results_to_csv, extract_wear_number
    from visualization import create_tooth1_analysis_graph, display_tooth1_summary_stats
    
    # Get tooth1 configuration
    tooth1_config = get_config("tooth1")
    actual_measurements = tooth1_config.actual_measurements
    GEAR_MODULE = tooth1_config.GEAR_SPECS['module']
    TOOTH_COUNT = tooth1_config.GEAR_SPECS['tooth_count']
    STANDARD_TOOTH_HEIGHT = tooth1_config.GEAR_SPECS['tooth_height']
    MAX_THEORETICAL_WEAR = tooth1_config.MAX_THEORETICAL_WEAR
    EXPECTED_TOOTH_COUNT = tooth1_config.EXPECTED_TOOTH_COUNT
    
    def main():
        """
        Main function to run tooth 1 wear analysis
        """
        print("🔧 TOOTH 1 WEAR DEPTH ANALYSIS")
        print("=" * 40)
        
        print(f"🏭 Gear Specifications: KHK SS3-35")
        print(f"   Module: {GEAR_MODULE} mm, Teeth: {TOOTH_COUNT}")
        print(f"   Standard Tooth Height: {STANDARD_TOOTH_HEIGHT:.2f} mm")
        print(f"   Max Theoretical Wear: {MAX_THEORETICAL_WEAR:.1f} µm")
        print(f"   Expected Tooth Count: {EXPECTED_TOOTH_COUNT}")
        print(f"📊 Actual measurements available for {len(actual_measurements)} cases")
        
        # Run tooth 1 analysis
        tooth1_results = analyze_tooth1_wear_depth()
        
        if tooth1_results:
            # Enforce monotonicity for tooth1 analysis
            from data_utils import enforce_monotonicity
            tooth1_results = enforce_monotonicity(tooth1_results, analysis_type="tooth1")
            
            # Save results to CSV file (both long format and table format automatically)
            save_results_to_csv(tooth1_results, analysis_type="tooth1")
            
            # Create visualization (commented out to avoid duplication with plot_results.py)
            # create_tooth1_analysis_graph(tooth1_results)
            
            # Display summary statistics
            display_tooth1_summary_stats(tooth1_results)
            
            # Calculate precision
            correct_predictions = 0
            total_predictions = 0
            
            for result in tooth1_results:
                wear_case = result["wear_case"]
                predicted_depth = result["wear_depth_um"]
                
                if wear_case in actual_measurements:
                    actual_depth = actual_measurements[wear_case]
                    error_percentage = abs(predicted_depth - actual_depth) / actual_depth * 100
                    
                    if error_percentage <= 20:
                        correct_predictions += 1
                    total_predictions += 1
            
            if total_predictions > 0:
                precision = (correct_predictions / total_predictions) * 100
                print(f"📊 Tooth 1 Precision: {precision:.1f}% ({correct_predictions}/{total_predictions})")
            else:
                print("📊 Tooth 1 Precision: No predictions to evaluate")
            
            print(f"📊 Tooth 1 Analysis Summary:")
            print(f"   Total wear cases analyzed: {len(tooth1_results)}")
            print(f"   Wear depth range: {min([r['wear_depth_um'] for r in tooth1_results]):.1f} - {max([r['wear_depth_um'] for r in tooth1_results]):.1f} µm")
        
        print("\n🎉 TOOTH 1 ANALYSIS COMPLETED!")
        print("=" * 40)
    
    if __name__ == "__main__":
        main()
        
except Exception as e:
    print(f"❌ Error occurred: {type(e).__name__}: {str(e)}")
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
