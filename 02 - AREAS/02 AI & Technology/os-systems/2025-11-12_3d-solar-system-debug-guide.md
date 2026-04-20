---
title: "3D Solar System Debug Guide"
date: 2025-11-12
tags:
  - machine-learning
  - obsidian
  - projects
  - web-dev
source: qwen-export
model: qwen3-max-2025-10-20
---

# 3D Solar System Debug Guide

**Date:** 2025-11-12  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[Machine-Learning]] · [[Obsidian]] · [[Projects]] · [[Web-Dev]]

---

### 🧑 You

Help me<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Solar System</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
        #info {
            position: absolute;
            top: 10px;
            width: 100%;
            text-align: center;
            color: white;
            font-family: monospace;
            font-size: 14px;
            z-index: 100;
        }
    </style>
</head>
<body>
    <div id="info">
        3D Solar System<br/>
        (Left Click + Drag to Rotate | Scroll to Zoom | Right Click + Drag to Pan)
    </div>

    <!-- 1. Import Three.js and OrbitControls from a CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js  "></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js  "></script>

    <script>
        // 2. Basic Setup: Scene, Camera, Renderer
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x000814); // Dark space background

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 30, 50); // Position camera to view the system

        const renderer = new THREE.WebGLRenderer({ antialias: true }); // antialias for smoother edges
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // 3. Lighting
        // Ambient light provides a soft, overall light source
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
        scene.add(ambientLight);

        // Point light emulates the sun's light
        const sunLight = new THREE.PointLight(0xffffff, 2, 300);
        sunLight.position.set(0, 0, 0);
        scene.add(sunLight);

        // 4. Create Celestial Bodies
        const planets = [];

        // The Sun
        const sunGeometry = new THREE.SphereGeometry(5, 32, 32);
        const sunMaterial = new THREE.MeshBasicMaterial({ 
            color: 0xffff00,
            emissive: 0xffff00, // Makes the sun glow
            emissiveIntensity: 1
        });
        const sun = new THREE.Mesh(sunGeometry, sunMaterial);
        scene.add(sun);

        // Planet Data: name, color, size, distance from sun, orbital speed
        const planetData = [
            { name: 'Mercury', color: 0x8c8c8c, size: 0.4, distance: 10, speed: 0.04 },
            { name: 'Venus', color: 0xffc649, size: 0.9, distance: 15, speed: 0.03 },
            { name: 'Earth', color: 0x4169e1, size: 1, distance: 20, speed: 0.02 },
            { name: 'Mars', color: 0xcd5c5c, size: 0.5, distance: 25, speed: 0.018 },
            { name: 'Jupiter', color: 0xdaa520, size: 2.5, distance: 35, speed: 0.01 },
            { name: 'Saturn', color: 0xf4e99b, size: 2.2, distance: 45, speed: 0.008 },
            { name: 'Uranus', color: 0x4fd0e7, size: 1.5, distance: 55, speed: 0.006 },
            { name: 'Neptune', color: 0x4b70dd, size: 1.4, distance: 65, speed: 0.005 }
        ];

        // Helper function to create a planet
        function createPlanet(data) {
            const geometry = new THREE.SphereGeometry(data.size, 32, 32);
            const material = new THREE.MeshStandardMaterial({ color: data.color });
            const planet = new THREE.Mesh(geometry, material);

            // Store orbital data for animation
            planet.userData = { 
                distance: data.distance, 
                speed: data.speed, 
                angle: Math.random() * Math.PI * 2 // Start at a random angle
            };
            
            return planet;
        }

        // Create and add planets to the scene
        planetData.forEach(data => {
            const planet = createPlanet(data);
            scene.add(planet);
            planets.push(planet);
        });
        
        // Add Saturn's Rings
        const saturn = planets.find(p => p.userData.distance === 45);
        const ringGeometry = new THREE.RingGeometry(3, 5, 64);
        const ringMaterial = new THREE.MeshBasicMaterial({ 
            color: 0xf4e99b, 
            side: THREE.DoubleSide, 
            opacity: 0.7, 
            transparent: true 
        });
        const saturnRings = new THREE.Mesh(ringGeometry, ringMaterial);
        saturnRings.rotation.x = Math.PI / 2; // Lay rings flat
        saturn.add(saturnRings); // Attach rings to Saturn


        // 5. Add Orbit Controls
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true; // Makes camera movement smooth
        controls.dampingFactor = 0.05;
        controls.minDistance = 10;
        controls.maxDistance = 200;

        // 6. Animation Loop
        function animate() {
            requestAnimationFrame(animate);

            // Rotate the Sun
            sun.rotation.y += 0.005;

            // Orbit and rotate the planets
            planets.forEach(planet => {
                const data = planet.userData;
                data.angle += data.speed;

                // Calculate new position based on angle and distance
                planet.position.x = Math.cos(data.angle) * data.distance;
                planet.position.z = Math.sin(data.angle) * data.distance;

                // Rotate the planet on its own axis
                planet.rotation.y += 0.01;
            });

            // Update the controls
            controls.update();

            // Render the scene from the perspective of the camera
            renderer.render(scene, camera);
        }

        // 7. Handle Window Resizing
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        // Start the animation
        animate();

    </script>
</body>
</html>

---

### 🧑 You

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Solar System</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
        #info {
            position: absolute;
            top: 10px;
            width: 100%;
            text-align: center;
            color: white;
            font-family: monospace;
            font-size: 14px;
            z-index: 100;
        }
    </style>
</head>
<body>
    <div id="info">
        3D Solar System<br/>
        (Left Click + Drag to Rotate | Scroll to Zoom | Right Click + Drag to Pan)
    </div>

    <!-- 1. Import Three.js and OrbitControls from a CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js  "></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js  "></script>

    <script>
        // 2. Basic Setup: Scene, Camera, Renderer
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x000814); // Dark space background

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 30, 50); // Position camera to view the system

        const renderer = new THREE.WebGLRenderer({ antialias: true }); // antialias for smoother edges
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // 3. Lighting
        // Ambient light provides a soft, overall light source
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
        scene.add(ambientLight);

        // Point light emulates the sun's light
        const sunLight = new THREE.PointLight(0xffffff, 2, 300);
        sunLight.position.set(0, 0, 0);
        scene.add(sunLight);

        // 4. Create Celestial Bodies
        const planets = [];

        // The Sun
        const sunGeometry = new THREE.SphereGeometry(5, 32, 32);
        const sunMaterial = new THREE.MeshBasicMaterial({ 
            color: 0xffff00,
            emissive: 0xffff00, // Makes the sun glow
            emissiveIntensity: 1
        });
        const sun = new THREE.Mesh(sunGeometry, sunMaterial);
        scene.add(sun);

        // Planet Data: name, color, size, distance from sun, orbital speed
        const planetData = [
            { name: 'Mercury', color: 0x8c8c8c, size: 0.4, distance: 10, speed: 0.04 },
            { name: 'Venus', color: 0xffc649, size: 0.9, distance: 15, speed: 0.03 },
            { name: 'Earth', color: 0x4169e1, size: 1, distance: 20, speed: 0.02 },
            { name: 'Mars', color: 0xcd5c5c, size: 0.5, distance: 25, speed: 0.018 },
            { name: 'Jupiter', color: 0xdaa520, size: 2.5, distance: 35, speed: 0.01 },
            { name: 'Saturn', color: 0xf4e99b, size: 2.2, distance: 45, speed: 0.008 },
            { name: 'Uranus', color: 0x4fd0e7, size: 1.5, distance: 55, speed: 0.006 },
            { name: 'Neptune', color: 0x4b70dd, size: 1.4, distance: 65, speed: 0.005 }
        ];

        // Helper function to create a planet
        function createPlanet(data) {
            const geometry = new THREE.SphereGeometry(data.size, 32, 32);
            const material = new THREE.MeshStandardMaterial({ color: data.color });
            const planet = new THREE.Mesh(geometry, material);

            // Store orbital data for animation
            planet.userData = { 
                distance: data.distance, 
                speed: data.speed, 
                angle: Math.random() * Math.PI * 2 // Start at a random angle
            };
            
            return planet;
        }

        // Create and add planets to the scene
        planetData.forEach(data => {
            const planet = createPlanet(data);
            scene.add(planet);
            planets.push(planet);
        });
        
        // Add Saturn's Rings
        const saturn = planets.find(p => p.userData.distance === 45);
        const ringGeometry = new THREE.RingGeometry(3, 5, 64);
        const ringMaterial = new THREE.MeshBasicMaterial({ 
            color: 0xf4e99b, 
            side: THREE.DoubleSide, 
            opacity: 0.7, 
            transparent: true 
        });
        const saturnRings = new THREE.Mesh(ringGeometry, ringMaterial);
        saturnRings.rotation.x = Math.PI / 2; // Lay rings flat
        saturn.add(saturnRings); // Attach rings to Saturn


        // 5. Add Orbit Controls
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true; // Makes camera movement smooth
        controls.dampingFactor = 0.05;
        controls.minDistance = 10;
        controls.maxDistance = 200;

        // 6. Animation Loop
        function animate() {
            requestAnimationFrame(animate);

            // Rotate the Sun
            sun.rotation.y += 0.005;

            // Orbit and rotate the planets
            planets.forEach(planet => {
                const data = planet.userData;
                data.angle += data.speed;

                // Calculate new position based on angle and distance
                planet.position.x = Math.cos(data.angle) * data.distance;
                planet.position.z = Math.sin(data.angle) * data.distance;

                // Rotate the planet on its own axis
                planet.rotation.y += 0.01;
            });

            // Update the controls
            controls.update();

            // Render the scene from the perspective of the camera
            renderer.render(scene, camera);
        }

        // 7. Handle Window Resizing
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        // Start the animation
        animate();

    </script>
</body>
</html>

---
