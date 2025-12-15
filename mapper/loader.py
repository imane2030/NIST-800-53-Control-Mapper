import pandas as pd
from .models import Control, Mapping

def load_controls(path: str, framework: str):
    """Load controls from CSV file."""
    df = pd.read_csv(path)
    controls = []
    
    for _, row in df.iterrows():
        controls.append(
            Control(
                framework=framework,
                id=row["id"],
                name=row["name"],
                description=row.get("description", ""),
            )
        )
    
    return controls

def load_mappings(path: str):
    """Load control mappings from CSV file."""
    df = pd.read_csv(path)
    mappings = []
    
    for _, row in df.iterrows():
        mappings.append(
            Mapping(
                source_framework=row["source_framework"],
                source_id=row["source_id"],
                target_framework=row["target_framework"],
                target_id=row["target_id"],
                relationship=row.get("relationship", "related"),
            )
        )
    
    return mappings
