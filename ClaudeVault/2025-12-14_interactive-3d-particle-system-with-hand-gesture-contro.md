---
title: "Interactive 3D particle system with hand gesture control"
date: 2025-12-14
tags:
  - python
  - linux
  - buddhism
  - stock-market
source: claude-export
---

# Interactive 3D particle system with hand gesture control

**Date:** 2025-12-14  
**Topics:** [[Python]] · [[Linux]] · [[Buddhism]] · [[Stock-Market]]

---

### 🧑 You

el.cine
@EHuanglu
·
Dec 1
prompts:  Create a real-time interactive 3D particle system with Three.js.  requirements:  1. Control the scaling and expansion of the particle group by detecting the tension and closing of both hands through the camera.  2. Provide panels that can choose hearts/flowers/saturn/Buddha statues/fireworks and other templates  3. Support the colour selector to adjust the particle colour  4. Particles need to respond to gesture changes in real time. The interface is simple and modern.  5. The interface is simple and modern

---

### 🤖 Claude

I'll create an interactive 3D particle system with hand gesture control using Three.js and MediaPipe for hand tracking.

{'type': 'text', 'text': 'OK', 'uuid': 'a9b1d05e-4360-4f39-9444-fd443699ac36'}

I've created a real-time interactive 3D particle system with all the requested features:

**Key Features:**

1. **Hand Gesture Control** - Uses MediaPipe to detect both hands through your camera. Move your hands apart to expand the particle system, bring them together to shrink it.

2. **Multiple Templates** - Choose from 5 different particle formations:
   - Heart shape
   - Flower pattern
   - Saturn with rings
   - Buddha statue silhouette
   - Fireworks bursts

3. **Color Customization** - Interactive color picker to change particle colors in real-time

4. **Real-time Response** - Particles scale smoothly based on the distance between your hands

5. **Modern UI** - Clean, dark-themed interface with a control panel on the right side

**How to Use:**
1. Click "Start Camera" to enable hand tracking
2. Allow camera access when prompted
3. Show both hands to the camera
4. Move hands apart/together to control particle scale
5. Select different templates and colors from the control panel

The system provides live feedback showing your hand positions and the current scale factor. The particles rotate automatically for a dynamic 3D effect!

---
