"""
Picture Analysis Submenu Module
Handles all picture analysis related menu options and functionality
"""

import os
import sys
import subprocess
import csv
import pandas as pd

# Import modular components
from data_loader import load_analysis_data
from visualization import plot_results
from picture_results_display import display_integrated_results_table, display_summary_statistics

def analysis_menu():
    """Display submenu for analysis"""
    while True:
        print("\n ANALYSIS MENU")
        print("=" * 35)
        print("1. Database Process")
        print("2. Show Results")
        print("3. Exit")
        
        try:
            choice = input(f"\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                display_database_process_menu()
                    
            elif choice == "2":
                display_show_results_menu()
                    
            elif choice == "3":
                break
                
            else:
                print("❌ Invalid choice. Please enter a number between 1-3.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")

def display_database_process_menu():
    """Display menu for database processing """
    while True:
        print("\n🔧 DATABASE PROCESS MENU")
        print("=" * 35)
        print("1. Run Tooth 1 Analysis")
        print("2. Run Integrated Gear Wear Analysis")
        print("3. Run Complete Analysis (Tooth 1 + All Teeth)")
        print("4. Return to Analysis Menu")
        
        try:
            choice = input(f"\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n🔧 Running Tooth 1 Analysis...")
                result = run_tooth1_analysis()
                if result:
                    print("✅ Tooth 1 analysis completed successfully!")
                else:
                    print("❌ Tooth 1 analysis failed!")
                    
            elif choice == "2":
                print("\n🔧 Running Integrated Gear Wear Analysis...")
                result = run_integrated_gear_wear_analysis()
                if result:
                    print("✅ Integrated gear wear analysis completed successfully!")
                else:
                    print("❌ Integrated gear wear analysis failed!")
                    
            elif choice == "3":
                print("\n🔧 Running Complete Analysis...")
                print("Step 1: Tooth 1 Analysis...")
                result1 = run_tooth1_analysis()
                if result1:
                    print("✅ Tooth 1 analysis completed!")
                    print("Step 2: Integrated Gear Wear Analysis...")
                    result2 = run_integrated_gear_wear_analysis()
                    if result2:
                        print("✅ Complete analysis finished successfully!")
                    else:
                        print("❌ Integrated analysis failed!")
                else:
                    print("❌ Tooth 1 analysis failed!")
                    
            elif choice == "4":
                break
                
            else:
                print("❌ Invalid choice. Please enter a number between 1-4.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")

def display_show_results_menu():
    """Display menu for showing results"""
    while True:
        print("\n📊 SHOW RESULTS MENU")
        print("=" * 35)
        print("1. Show Integrated Results Table")
        print("2. Plot Results")
        print("3. Return to Analysis Menu")
        
        try:
            choice = input(f"\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                show_integrated_results_table()
                    
            elif choice == "2":
                plot_results()
                    
            elif choice == "3":
                break
                
            else:
                print("❌ Invalid choice. Please enter a number between 1-3.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")

def run_tooth1_analysis():
    """Run tooth 1 wear depth analysis"""
    try:
        # Run the modular tooth 1 analysis script
        script_path = "Analyze_tooth1.py"
        if not os.path.exists(script_path):
            print(f"❌ Script not found: {script_path}")
            return False
        
        print(f"🔧 Executing: {script_path}")
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, 
                              text=True,
                              encoding='utf-8',
                              env=env)
        
        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("⚠️ Warnings/Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            return True
        else:
            print(f"❌ Tooth 1 analysis failed with error:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error running tooth 1 analysis: {str(e)}")
        return False

def run_integrated_gear_wear_analysis():
    """Run integrated gear wear analysis"""
    try:
        # Run the new modular gear wear analysis script
        script_path = "Analyze_all_teeth.py"
        if not os.path.exists(script_path):
            print(f"❌ Script not found: {script_path}")
            return False
        
        print(f"🔧 Executing: {script_path}")
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, 
                              text=True,
                              encoding='utf-8',
                              env=env)
        
        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("⚠️ Warnings/Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ Gear wear analysis completed successfully!")
            return True
        else:
            print(f"❌ Gear wear analysis failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running gear wear analysis: {str(e)}")
        return False



def plot_results():
    """Plot results from CSV files using modular components"""
    try:
        # Load data using modular data loader
        single_tooth_data, all_teeth_data = load_analysis_data()
        
        if not single_tooth_data or not all_teeth_data:
            print("❌ No data available for plotting")
            return
        
        # Use modular visualization component
        import subprocess
        import sys
        
        # Run the plot_results.py script in current directory
        if not os.path.exists("plot_results.py"):
            print(f"❌ plot_results.py script not found")
            return
        
        # Run the plot_results.py script
        result = subprocess.run([sys.executable, "plot_results.py"], 
                              capture_output=True, 
                              text=True)
        
        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("⚠️ Warnings/Errors:")
            print(result.stderr)
        
    except Exception as e:
        print(f"❌ Error plotting results: {str(e)}")

def show_integrated_results_table():
    """Show integrated results table combining single tooth and all teeth data"""
    try:
        # Load data using modular data loader
        single_tooth_data, all_teeth_data = load_analysis_data()
        
        if not single_tooth_data:
            print("❌ No single tooth data to display")
            return
        
        # Use modular results display component
        display_integrated_results_table(single_tooth_data, all_teeth_data)
        display_summary_statistics(single_tooth_data, all_teeth_data)
        
    except Exception as e:
        print(f"❌ Error showing integrated results: {str(e)}")

# Legacy functions for backward compatibility (simplified)
def display_results_menu(results):
    """Legacy function - redirect to new menu"""
    print("⚠️ This function has been replaced. Use 'Show Results' from the main analysis menu.")
    display_show_results_menu()

def display_wear_level_summary(results):
    """Legacy function - redirect to new menu"""
    print("⚠️ This function has been replaced. Use 'Show Results' from the main analysis menu.")
    display_show_results_menu()

def display_overall_assessment(results):
    """Legacy function - redirect to new menu"""
    print("⚠️ This function has been replaced. Use 'Show Results' from the main analysis menu.")
    print("Please use the new integrated gear wear analysis system.")

def display_database_analysis_menu():
    """Legacy function - redirect to new menu"""
    print("⚠️ This function has been replaced. Use 'Database Process' from the main analysis menu.")
    display_database_process_menu()

# Main entry point
if __name__ == "__main__":
    print("🔧 WEAR IMAGE PROCESS - ANALYSIS TOOL")
    print("=" * 50)
    print("Welcome to the Gear Wear Analysis System!")
    print()
    
    # Start the main analysis menu
    analysis_menu()