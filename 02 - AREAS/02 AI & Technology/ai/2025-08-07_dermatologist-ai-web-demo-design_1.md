---
title: "Dermatologist AI Web Demo Design"
date: 2025-08-07
tags:
  - machine-learning
  - data-analysis
  - web-dev
  - game-design
source: claude-export
---

# Dermatologist AI Web Demo Design

**Date:** 2025-08-07  
**Topics:** [[Machine-Learning]] · [[Data-Analysis]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Create a single-page demo website for the open-source GitHub project "Dermatologist AI" (https://github.com/udacity/dermatologist-ai). The website should include:
**1. Hero Section:**
* Title: “Dermatologist AI”
* Subtitle: “AI-Powered Skin Lesion Classification Demo”
* Short description: “This demo is inspired by the Dermatologist AI project, which classifies skin lesions as melanoma, nevus, or seborrheic keratosis using deep learning.”
**2. Image Upload and Prediction Section:**
* An area to upload a skin lesion image (accept only image files).
* A “Predict” button (the backend isn’t live, so for demo just generate random probabilities for each class on click).
* Show a table or card with the *probabilities* for “Melanoma”, “Nevus”, and “Seborrheic Keratosis” after prediction.
**3. Visualization:**
* Show the predicted probabilities as a simple bar chart (use JavaScript/Chart.js or CSS bars).
**4. Info Section:**
* How the real project works: “The actual model is trained on ISIC skin lesion dataset and uses a CNN to classify uploaded images.”
* Link to the GitHub repo.
**5. Fully Styled:**
* Use attractive, modern CSS; responsive layout.
* Buttons, file input, and results should be visually appealing.
**6. Pure Front-End:**
* All HTML, CSS, and JavaScript must be self-contained in a single file.
* No backend required.
* Show a demo image or placeholder if upload is skipped

---

### 🤖 Claude

I'll create a modern, fully-functional single-page demo website for the Dermatologist AI project. This will include all the features you requested with an attractive design and interactive elements.

{'type': 'text', 'text': 'OK', 'uuid': '0b8981f1-cf83-45fa-9ddd-14fc5f312ec3'}
I've created a comprehensive single-page demo website for the Dermatologist AI project with all the features you requested:

## Key Features:

**🎯 Hero Section**
- Attractive gradient background with the project title and description
- Clear branding and purpose statement

**📤 Image Upload & Prediction**
- Drag-and-drop file upload area with visual feedback
- Image preview functionality
- "Predict" button with loading animation
- Generates realistic random probabilities for demo purposes

**📊 Results Visualization**
- Clean table showing probabilities for all three conditions
- Animated progress bars for visual confidence levels
- Interactive doughnut chart using Chart.js
- Smooth animations and transitions

**ℹ️ Information Section**
- Explains how the real project works
- Describes each skin lesion type
- Direct link to the GitHub repository

**🎨 Modern Design**
- Responsive layout that works on all devices
- Gradient backgrounds and smooth hover effects
- Professional card-based layout
- Accessible color scheme and typography

## Technical Implementation:
- **Single HTML file** with embedded CSS and JavaScript
- **No backend required** - generates random probabilities for demonstration
- **Chart.js integration** for professional data visualization
- **Drag-and-drop file handling** with image preview
- **Responsive design** for mobile and desktop
- **Loading states** and smooth animations

The demo automatically shows sample results after 3 seconds if no image is uploaded, making it immediately engaging for visitors. Users can upload their own images to see new random predictions generated each time they click "Predict".

---
