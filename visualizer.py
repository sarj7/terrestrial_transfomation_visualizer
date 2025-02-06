import geopandas as gpd
import plotly.graph_objects as go
import plotly.io as pio
import os

def get_file_path(prompt):
    """Prompt user for file path with validation."""
    while True:
        file_path = input(prompt).strip()
        if os.path.exists(file_path):
            return file_path
        print("File not found. Please check the path and try again.")

def create_interactive_map(historical_map_path, current_map_path):
    """
    Create an interactive map visualization of urban transformation.

    Parameters:
    - historical_map_path: Path to the historical map/shapefile
    - current_map_path: Path to the current map/shapefile

    Returns:
    - Interactive Plotly figure
    """
    try:
        # Read historical map data
        historical_gdf = gpd.read_file(historical_map_path)
        current_gdf = gpd.read_file(current_map_path)

        # Ensure both are in WGS84 coordinate system
        historical_gdf = historical_gdf.to_crs(epsg=4326)
        current_gdf = current_gdf.to_crs(epsg=4326)

        # Create base figure
        fig = go.Figure()

        # Add historical map layer
        for idx, row in historical_gdf.iterrows():
            if row.geometry:
                # Handle different geometry types
                if row.geometry.geom_type == 'Polygon':
                    lons, lats = row.geometry.exterior.xy
                    fig.add_trace(go.Scattermapbox(
                        mode='lines',
                        lon=list(lons),
                        lat=list(lats),
                        fill='toself',
                        fillcolor='rgba(255,0,0,0.3)',
                        line=dict(color='red', width=2),
                        name=f'Historical Area {idx}'
                    ))

        # Add current map layer
        for idx, row in current_gdf.iterrows():
            if row.geometry:
                # Handle different geometry types
                if row.geometry.geom_type == 'Polygon':
                    lons, lats = row.geometry.exterior.xy
                    fig.add_trace(go.Scattermapbox(
                        mode='lines',
                        lon=list(lons),
                        lat=list(lats),
                        fill='toself',
                        fillcolor='rgba(0,0,255,0.3)',
                        line=dict(color='blue', width=2),
                        name=f'Current Area {idx}'
                    ))

        # Update layout for mapbox
        fig.update_layout(
            title='Urban Transformation Interactive Map',
            mapbox_style="open-street-map",
            mapbox=dict(
                center=dict(
                    lat=historical_gdf.geometry.centroid.y.mean(),
                    lon=historical_gdf.geometry.centroid.x.mean()
                ),
                zoom=10
            ),
            showlegend=True,
            height=800,
            margin={"r":0,"t":50,"l":0,"b":0}
        )

        return fig

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_interactive_map(fig, output_path='urban_transformation_map.html'):
    """
    Save the interactive map as an HTML file.

    Parameters:
    - fig: Plotly figure
    - output_path: Path to save the interactive map
    """
    if fig:
        pio.write_html(fig, file=output_path)
        print(f"Interactive map saved to {output_path}")

def main():
    # Prompt user for map paths
    print("Urban Transformation Map Visualizer")
    historical_map_path = get_file_path("Enter path to historical map shapefile: ")
    current_map_path = get_file_path("Enter path to current map shapefile: ")

    # Create interactive map
    interactive_map = create_interactive_map(historical_map_path, current_map_path)

    # Option to show map
    if interactive_map:
        interactive_map.show()

        # Option to save map
        save_choice = input("Do you want to save the interactive map? (yes/no): ").lower()
        if save_choice in ['yes', 'y']:
            default_path = 'urban_transformation_map.html'
            save_path = input(f"Enter save path (press Enter for default: {default_path}): ").strip()
            save_path = save_path if save_path else default_path
            save_interactive_map(interactive_map, save_path)

if __name__ == "__main__":
    main()

