import sys
from pathlib import Path

# Add project root to Python path so tests can import quick_calc
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))