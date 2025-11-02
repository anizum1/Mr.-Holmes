#!/bin/bash
# OSINT Tool Installation Script for Linux

echo "======================================"
echo "  OSINT Tool Installation Script"
echo "======================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Found Python $PYTHON_VERSION"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

echo "✅ pip3 is available"

# Create virtual environment (recommended)
echo ""
echo "Creating virtual environment..."
python3 -m venv osint_env

echo "✅ Virtual environment created"

# Activate virtual environment
source osint_env/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Make scripts executable
chmod +x osint_tool.py
chmod +x osint_cli.py
chmod +x advanced_utils.py

echo ""
echo "======================================"
echo "  Installation Complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Activate virtual environment:"
echo "   source osint_env/bin/activate"
echo ""
echo "2. Configure API keys:"
echo "   python3 osint_tool.py"
echo "   (This will create config.json template)"
echo ""
echo "3. Edit config.json and add your API credentials"
echo ""
echo "4. Run the tool:"
echo "   python3 osint_cli.py --help"
echo ""
echo "For detailed usage instructions, see README.md"
echo ""
