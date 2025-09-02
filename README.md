# ⚙️ Gear Wear Analysis System

A comprehensive Python-based system for analyzing gear wear patterns using computer vision and machine learning techniques. This system processes gear images to detect, measure, and analyze wear patterns, providing both single-tooth and comprehensive all-teeth analysis capabilities.

## ✨ Features

- **🔍 Single Tooth Analysis**: Detailed wear analysis for individual gear teeth
- **⚙️ All Teeth Analysis**: Comprehensive analysis across entire gear systems
- **📊 Table Format Output**: Results automatically formatted in easy-to-read table format
- **🖼️ Image Processing**: Advanced computer vision algorithms for wear detection
- **📈 Visualization**: Interactive plots and graphs for result analysis
- **🎯 Physical Calibration**: Support for physical scale calibration (µm/px)
- **📋 Batch Processing**: Process multiple images efficiently
- **💾 Data Export**: CSV export with structured table format

## 🏗️ Project Structure

```
Picture/
├── Main.py                          # Main application entry point
├── config.py                        # Configuration management
├── data_loader.py                   # Data loading and parsing
├── data_utils.py                    # Data utilities and CSV operations
├── image_processor.py               # Core image processing
├── wear_analyzer.py                 # Wear analysis algorithms
├── tooth1_analyzer.py               # Single tooth analysis
├── tooth1_image_processor.py        # Single tooth image processing
├── tooth1_ml_engine.py              # Machine learning engine
├── batch_processor.py               # Batch processing utilities
├── picture_results_display.py       # Results display and visualization
├── plot_results.py                  # Plotting and charting
├── visualization.py                  # Visualization utilities
├── gear_parameters.py               # Gear-specific parameters
├── Analyze_all_teeth.py             # All teeth analysis script
├── Analyze_tooth1.py                # Single tooth analysis script
├── database/                        # Image database
│   ├── Healthy.png                  # Healthy gear reference
│   ├── Wear1.png - Wear35.png      # Wear case images
│   └── Wear depth measurments/     # Calibrated measurement images
├── all_teeth_results.csv            # All teeth analysis results
├── single_tooth_results.csv         # Single tooth analysis results
└── ground_truth_measurements.csv    # Reference measurements
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Manual Installation (if requirements.txt fails)
```bash
pip install opencv-python
pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-image
pip install scipy
```

## 📖 Usage

### 1. Main Application
Run the main application with the interactive menu:
```bash
python Main.py
```

### 2. Direct Script Execution
Run specific analysis scripts directly:

**Single Tooth Analysis:**
```bash
python Analyze_tooth1.py
```

**All Teeth Analysis:**
```bash
python Analyze_all_teeth.py
```

### 3. Menu Options
The main application provides these options:
- **1. Run Tooth1 Analysis** - Analyze single tooth wear patterns
- **2. Run Integrated Gear Wear Analysis** - Comprehensive gear analysis
- **3. Show Integrated Results Table** - Display results in table format
- **4. Show Summary Statistics** - View statistical summaries
- **5. Exit** - Close the application

## 🔧 Configuration

### Key Parameters
- **Target µm/px**: Default scale factor (6.0 µm/px)
- **Reference Diameter**: Physical reference for calibration
- **Analysis Type**: Single tooth or all teeth
- **Database Path**: Path to image database

### Configuration File
Edit `config.py` to modify:
- File paths
- Analysis parameters
- Visualization settings
- Database locations

## 📊 Output Format

### Results Structure
Results are automatically saved in table format:

**Single Tooth Results:**
```
W1,W2,W3,W4,W5,...
250.1,249.8,250.0,249.7,250.7,...
```

**All Teeth Results:**
```
Tooth,W1,W2,W3,W4,W5,...
1,250.1,249.8,250.0,249.7,250.7,...
2,250.0,249.9,250.1,249.8,250.6,...
...
```

### File Locations
- `single_tooth_results.csv` - Single tooth analysis results
- `all_teeth_results.csv` - All teeth analysis results
- `*.png` - Generated visualization plots

## 🧪 Analysis Types

### Single Tooth Analysis
- Processes individual gear teeth
- Compares against healthy reference
- Generates wear depth measurements
- Creates detailed analysis plots

### All Teeth Analysis
- Processes entire gear systems
- Generates comprehensive wear maps
- Provides statistical summaries
- Creates integrated visualizations

## 🔬 Technical Details

### Image Processing Pipeline
1. **Preprocessing**: Image enhancement and noise reduction
2. **Contour Detection**: Edge detection and contour extraction
3. **Feature Extraction**: Wear pattern identification
4. **Measurement**: Depth and area calculations
5. **Analysis**: Statistical and comparative analysis

### Machine Learning Features
- Wear pattern recognition
- Anomaly detection
- Predictive modeling
- Feature engineering

## 🐛 Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all dependencies are installed
2. **Path Issues**: Check database path configuration
3. **Memory Issues**: Reduce image resolution for large datasets
4. **Calibration Errors**: Verify reference image scales

### Debug Mode
Enable debug output by modifying `config.py`:
```python
DEBUG_MODE = True
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- Scientific Python ecosystem for data analysis
- Research community for wear analysis methodologies

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

---

**Last Updated**: December 2024  
**Version**: 1.0.0  
**Python Version**: 3.8+
