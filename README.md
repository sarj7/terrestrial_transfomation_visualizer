# Urban Transformation Map Visualizer

## Overview
This Python application creates an interactive visualization of urban transformation by overlaying historical and current geospatial map data.

## Features
- Interactive map visualization
- Overlay of historical and current city maps
- Zoomable and pannable interface
- Save option for interactive HTML map

## Prerequisites
- Python 3.7+
- Required libraries:
  ```
  pip install geopandas plotly pyproj
  ```

## Supported File Formats
- Geospatial Shapefiles (.shp)
- Requires two separate shapefiles:
  1. Historical map data
  2. Current map data

## Installation
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script and follow the interactive prompts:
```bash
python urban_transformation_map.py
```

### Input Workflow
1. Enter path to historical map shapefile
2. Enter path to current map shapefile
3. Interactive map will automatically generate
4. Choose to save the map as HTML (optional)

## Example Input
- Historical Map: `/path/to/city_map_1990.shp`
- Current Map: `/path/to/city_map_2023.shp`

## Visualization Details
- Red overlay: Historical map boundaries
- Blue overlay: Current map boundaries
- Transparent layers allow comparison of urban changes

## Troubleshooting
- Ensure shapefiles are in WGS84 coordinate system
- Check file paths carefully
- Verify shapefile integrity before use

## Limitations
- Requires geospatial shapefiles
- Internet connection needed for base map
- Performance depends on map complexity

## Contributing
Contributions welcome! Please submit pull requests or open issues.

