# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains interactive HTML educational materials for Korean elementary school mathematics (5th grade, 2nd semester). The project creates engaging, animated presentations for teaching fraction multiplication concepts using visual models and interactive quizzes.

## Architecture and Structure

### Core Components

**Interactive HTML Presentations**: Self-contained HTML files that combine:
- CSS animations for step-by-step mathematical explanations
- JavaScript-based slide navigation and quiz interactions
- Responsive layouts optimized for widescreen displays
- Korean mathematical notation using custom CSS fraction classes

**Fraction Display System**: Custom CSS classes for mathematical notation:
- `.fraction` with `.num` and `.denom` for proper fraction rendering
- `.mixed-number` for combined whole numbers and fractions
- `.big-fraction` for enlarged mathematical expressions

**Layout Architecture**:
- `.horizontal-layout` with `.left-column` and `.right-column` for widescreen optimization
- `.side-by-side` and `.compact-grid` for flexible content arrangement
- Responsive breakpoints that convert to vertical layouts on smaller screens

**Animation Framework**:
- CSS keyframe animations for mathematical concept visualization
- JavaScript-controlled step-by-step progression
- Interactive controls for animation replay and step navigation

## Development Commands

### Local Development
```bash
# Open HTML files directly in browser for testing
# Recommended browsers: Chrome, Firefox, Safari, Edge

# For local server (if needed):
python -m http.server 8000
# Then access: http://localhost:8000/week_5_ko_el_5_2.html
```

### Content Processing
```bash
# Run fraction formatting script (for legacy content migration)
python fix_html.py
```

### Deployment
```bash
# Deploy to GitHub Pages
git add .
git commit -m "Update educational content"
git push origin master
# Accessible at: https://kubo63078.github.io/fun-math/
```

## Technical Implementation Notes

### Mathematical Content Structure
- Each lesson follows a consistent 18-slide format
- Slides include: introduction, learning objectives, concept explanation, practice problems, games, and summary
- Interactive elements use onclick handlers for immediate feedback
- Animation sequences are coordinated with JavaScript timing controls

### Localization Considerations
- All content is in Korean (ko locale)
- Mathematical expressions follow Korean educational standards
- Cultural references use familiar Korean contexts (초콜릿, 독서, etc.)
- Follows 2015 Revised Korean Elementary Curriculum

### Browser Compatibility Requirements
- Must work across desktop, tablet, and mobile browsers
- Supports touch interactions for mobile devices
- Uses modern CSS Grid and Flexbox for layout
- Animations use CSS transforms for performance

## Content Guidelines

### Educational Design Patterns
- Visual-first approach with animated step-by-step explanations
- Immediate feedback quizzes with celebration animations
- Real-world problem contexts (food sharing, reading progress)
- Progressive difficulty from concrete to abstract concepts

### Layout Optimization Principles
- Horizontal layouts maximize widescreen space utilization
- Content density balanced for elementary school attention spans
- Visual hierarchy using emojis, colors, and typography scales
- Consistent navigation patterns across all slides