---
title: "Interactive 3D particle system with hand gesture control"
date: 2025-12-03
tags:
  - python
  - data-analysis
  - buddhism
  - web-dev
source: claude-export
---

# Interactive 3D particle system with hand gesture control

**Date:** 2025-12-03  
**Topics:** [[Python]] · [[Data-Analysis]] · [[Buddhism]] · [[Web-Dev]]

---

### 🧑 You

prompts:  Create a real-time interactive 3D particle system with Three.js.  requirements:  1. Control the scaling and expansion of the particle group by detecting the tension and closing of both hands through the camera.  2. Provide panels that can choose hearts/flowers/saturn/Buddha statues/fireworks and other templates  3. Support the colour selector to adjust the particle colour  4. Particles need to respond to gesture changes in real time. The interface is simple and modern.  5. The interface is simple and modern

---

### 🤖 Claude

I'll create an interactive 3D particle system with hand gesture control using Three.js and MediaPipe for hand tracking. This will be a modern, feature-rich application with real-time gesture interaction.

{'type': 'text', 'text': 'OK', 'uuid': 'c2193a00-9c71-4065-b132-715c9d80dd73'}

I've created an interactive 3D particle system with real-time hand gesture control! Here's what I've included:

## Features:

**1. Gesture Control:**
- Uses MediaPipe Hands to track both hands via webcam
- Detects the distance between your hands in real-time
- Moving hands apart = particles expand
- Moving hands together = particles shrink
- Visual feedback with distance indicator

**2. Shape Templates:**
- ❤️ **Heart** - Classic heart shape
- 🌸 **Flower** - Petal pattern with radial symmetry
- 🪐 **Saturn** - Planet with ring system
- 🔥 **Buddha** - Meditative spiral form
- ✨ **Fireworks** - Multiple explosion bursts

**3. Color Customization:**
- Full color picker for any color
- Quick color presets for common choices
- Each template has a default suggested color

**4. Modern Interface:**
- Clean dark theme with purple/pink accents
- Smooth animations and transitions
- Real-time visual feedback
- Compact camera preview in corner
- Intuitive control panel

**5. Real-time Interaction:**
- Particles respond instantly to hand movements
- Smooth scaling animations
- Continuous rotation for better 3D visualization
- 2000 particles per shape for rich detail

**How to use:**
1. Click "Start Camera" to enable hand tracking
2. Show both hands to the camera
3. Move your hands closer/apart to control particle size
4. Switch between shapes and colors as desired

The system uses Three.js for 3D rendering and MediaPipe for accurate hand tracking, creating a magical, interactive experience!

---

### 🧑 You

> An error occurred while trying to run the generated artifact.
  > `THREE is not defined`
  

  Can you fix this error in `gesture-particle-system`?

---

### 🤖 Claude

{'type': 'text', 'text': 'OK', 'uuid': 'e75cc53a-0f41-4706-882d-9431805bf8f5'}

Fixed! I added the Three.js import at the top of the component. The artifact should now work correctly. Try clicking "Start Camera" to enable the gesture control feature!

---
