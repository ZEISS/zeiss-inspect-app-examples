# Agents.md - ZEISS INSPECT App Examples Repository

## Overview

This document provides guidance for AI agents interacting with the ZEISS INSPECT App Examples repository at https://github.com/ZEISS/zeiss-inspect-app-examples.

## Repository Purpose

Educational and inspirational examples for ZEISS INSPECT App development. These examples demonstrate how to extend ZEISS INSPECT software functionality through custom Python-based Apps.

**⚠️ Important**: Examples are for educational purposes only, not intended for productive use. Users utilize them at their own risk.

## What Can AI Agents Help With?

When users ask about this repository, agents can assist with:

1. **Understanding App Structure** - Explaining what ZEISS INSPECT Apps are and how they're organized
2. **Finding Relevant Examples** - Helping users locate examples for specific use cases
3. **Explaining Code Patterns** - Describing how the examples implement various features
4. **API Usage** - Guiding users on how to use the ZEISS INSPECT Python API
5. **Getting Started** - Providing steps to set up and use the examples

## Key Resources

- **Repository**: https://github.com/ZEISS/zeiss-inspect-app-examples
- **API Documentation**: https://zeiss.github.io/zeiss-inspect-app-api/
- **Examples Overview**: https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
- **Software Store**: https://software-store.zeiss.com
- **Training Center**: https://qualitytraining.zeiss.com/

## Example Categories Reference

### data_interfaces
**Purpose**: Accessing data from ZEISS INSPECT elements

**Examples**:
- `CheckResultsDataArray` - Accessing check result data via properties and data interfaces
- `ReferencePointsAndMeshData` - Accessing reference points and mesh data from Python
- `VolumeSectionImageData` - Accessing volume section image data

**Common User Questions**:
- How do I get check results programmatically?
- How do I access mesh data?
- How do I work with reference points?

### dialog_widgets
**Purpose**: Creating custom dialogs and handling user input

**Examples**:
- `ExplorerSelectedElementsInDialog` - Getting selected elements from explorer in dialogs

**Common User Questions**:
- How do I create custom UI dialogs?
- How do I get user-selected elements?
- How do I handle user input events?

### misc
**Purpose**: Miscellaneous utilities and transformations

**Examples**:
- `CSVExample` - Reading and writing CSV files from Apps
- `PointPixelTransformations` - Converting between 3D point and 2D pixel coordinates
- `IPCWebsocketExample` - Connect ZEISS INSPECT via external software via WebSocket protocol

**Common User Questions**:
- How do I import/export CSV data?
- How do I convert between 3D and 2D coordinates?

### scripted_actuals
**Purpose**: Building custom actual elements with Python

**Examples**:
- `TrimeshDeformMesh` - Generating custom surface elements, accessing mesh info, applying deformations

**Common User Questions**:
- How do I create [custom|parametric] geometric elements?
- How do I modify existing meshes?
- What are scripted actual elements?

### scripted_checks
**Purpose**: Building custom inspection checks with Python

**Examples**:
- `ScriptedCurveCheck` - Creating scalar curve checks with custom coordinate systems
- `ScriptedScalarCheck` - Creating basic scalar checks for elements
- `ScriptedSurfaceCheck` - Creating surface checks with custom coordinate systems and previews

**Common User Questions**:
- How do I create custom quality checks?
- What types of checks can I script?
- How do I use custom coordinate systems in checks?

### scripted_diagrams
**Purpose**: Creating custom visualization diagrams

### script_resources
**Purpose**: Accessing binary data and resources within Apps

### projects
**Purpose**: Example project files for testing

**Available Projects**:
- `zeiss_part_test_project` - Optically measured part with CAD, mesh, inspections
- `zeiss_part_test_measurement` - Optical measurement series and preliminary mesh
- `volume_test_project` - CT-related inspection test volume

## Technical Details for Agents

### App Structure
A ZEISS INSPECT App is a zip file containing:
- Python scripts
- Dialog (GUI) definitions (JSON)
- Templates
- Resources (text or binary data)
- App metadata

### Installation Methods
1. Download from ZEISS Quality Software Store
2. Clone repository → zip directory → import to ZEISS INSPECT

### Requirements
- **Software**: ZEISS INSPECT 2023 or later
- **Language**: Python
- **API**: ZEISS INSPECT Python API

### Common Code Patterns

```python
# Typical example structure
def function1():
    # Example code demonstrating feature 1
    pass

def function2():
    # -------------------------------------------------------------------------
    # Example code demonstrating feature 2
    # -------------------------------------------------------------------------
    pass

if __name__ == '__main__':
    result1 = function1()
    result2 = function2()
```

Key concepts of the example often are marked with # ------ comments in the code.

## Guidance for User Queries

### When Users Ask About:

**"How do I get started?"**
→ Direct to API Documentation and ZEISS INSPECT Python API Introduction section
→ Suggest cloning repository and reviewing relevant category
→ Recommend specific example based on their need

**"How do I access [specific data type]?"**
→ Point to `data_interfaces` category
→ Recommend specific example (CheckResultsDataArray, ReferencePointsAndMeshData, etc.)

**"How do I create custom [checks/elements/diagrams]?"**
→ Point to appropriate `scripted_*` category
→ Explain difference between actuals, checks, and diagrams

**"How do I create a [dialog/UI/GUI]?"**
→ https://zeiss.github.io/zeiss-inspect-app-api/

**"Can I use this in production?"**
→ Clarify these are educational examples only
→ Suggest adapting and testing thoroughly for production use

**"Where's the API documentation?"**
→ https://zeiss.github.io/zeiss-inspect-app-api/

## Common Workflows to Support

1. **Finding Relevant Example**
   - Understand user's goal
   - Match to appropriate category
   - Link to specific example documentation

2. **Understanding Example Code**
   - Explain Python API usage
   - Describe data access patterns
   - Clarify App-specific concepts

3. **Adapting Examples**
   - Guide on modifying examples
   - Explain parameters and options
   - Suggest testing approaches

4. **Troubleshooting**
   - Check ZEISS INSPECT version compatibility
   - Verify App structure
   - Direct to official documentation for complex issues

## Important Notes for Agents

- Always emphasize educational nature of examples
- Don't guarantee production readiness
- Direct complex API questions to official documentation
- Recommend testing in non-production environments
- Suggest ZEISS training for comprehensive learning

## Tags for Quick Reference

Examples are tagged with: data_interfaces, dialog_widgets, scripted_actuals, scripted_checks, mesh_data, reference_points, csv, transformations, coordinate_systems, surface_checks, curve_checks

## Support Escalation

For issues beyond example scope:
- **API Questions**: https://qualityforum.zeiss.com/forum/30-customizations-app-development/
- **App Development Documentation**: https://zeiss.github.io/zeiss-inspect-app-api/
- **Training**: https://training.gom.com
- **App Store**: https://software-store.zeiss.com