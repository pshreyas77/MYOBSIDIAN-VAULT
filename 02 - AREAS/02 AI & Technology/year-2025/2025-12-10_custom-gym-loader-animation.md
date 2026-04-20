---
title: "Custom Gym Loader Animation"
date: 2025-12-10
tags:
  - machine-learning
  - linux
  - web-dev
  - game-design
source: qwen-export
model: qwen3-max-2025-10-20
---

# Custom Gym Loader Animation

**Date:** 2025-12-10  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[Machine-Learning]] · [[Linux]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Gym Loader</title>
  <style>
    :root {
      --loader-color: #4CAF50; /* you can change this to suit your brand */
      --bar-width: 60px;
      --bar-height: 8px;
      --plate-size: 20px;
      --animation-duration: 1.2s;
    }

    body, html {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f5f5f5;
    }

    .gym-loader {
      position: relative;
      width: calc(var(--bar-width) + var(--plate-size) * 2);
      height: calc(var(--plate-size) * 1.5);
    }

    .bar {
      position: absolute;
      top: 50%;
      left: 50%;
      width: var(--bar-width);
      height: var(--bar-height);
      background-color: var(--loader-color);
      transform: translate(-50%, -50%);
      border-radius: 4px;
      transform-origin: center center;
      animation: bar-pump var(--animation-duration) ease-in-out infinite;
    }

    .plate {
      position: absolute;
      top: 50%;
      width: var(--plate-size);
      height: var(--plate-size);
      background-color: var(--loader-color);
      border-radius: 4px;
      transform: translateY(-50%);
    }

    .plate.left {
      left: 0;
      transform-origin: center center;
      animation: plate-pump-left var(--animation-duration) ease-in-out infinite;
    }

    .plate.right {
      right: 0;
      transform-origin: center center;
      animation: plate-pump-right var(--animation-duration) ease-in-out infinite;
    }

    @keyframes bar-pump {
      0%, 100% {
        transform: translate(-50%, -50%) scaleX(1);
      }
      50% {
        transform: translate(-50%, -50%) scaleX(0.85);
      }
    }

    @keyframes plate-pump-left {
      0%, 100% {
        transform: translateY(-50%) rotate(0deg);
      }
      50% {
        transform: translateY(-50%) rotate(-5deg) scale(0.9);
      }
    }

    @keyframes plate-pump-right {
      0%, 100% {
        transform: translateY(-50%) rotate(0deg);
      }
      50% {
        transform: translateY(-50%) rotate(5deg) scale(0.9);
      }
    }
  </style>
</head>
<body>

  <div class="gym-loader">
    <div class="bar"></div>
    <div class="plate left"></div>
    <div class="plate right"></div>
  </div>

</body>
</html>

---

### 🧑 You

Please create a loading animation using HTML and CSS that visually represents a gym or workout theme. The animation should be engaging and smooth, incorporating elements related to fitness—such as dumbbells, barbells, a person exercising, or other recognizable gym imagery. Focus on a clean, modern design that works well as a subtle loading indicator on a website or app. Provide the complete HTML and CSS code, well-organized and easy to integrate, and ensure the animation loops seamlessly with a polished, professional feel.

---

### 🧑 You

try diff style

---

### 🧑 You

make it dummble curl

---

### 🧑 You

not accurate

---

### 🧑 You

its good make it more professional and unique and it should work in light and dark mode differently

---
