
// Import Three.js and any necessary controls or loaders
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

// Define the main tree class
class ConversationTree {
  constructor() {
    this.treeContainer = document.getElementById('treeContainer');
    this.initializeScene();
    this.addEcoBot();
    this.setupInteractivity();
    this.animate();
  }

  // Sets up the Three.js scene
  initializeScene() {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, this.treeContainer.clientWidth / this.treeContainer.clientHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(this.treeContainer.clientWidth, this.treeContainer.clientHeight);
    this.treeContainer.appendChild(this.renderer.domElement);
  
    // Add lighting
    const ambientLight = new THREE.AmbientLight(0x404040); // soft white light
    this.scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
    directionalLight.position.set(0, 1, 0); // top down light
    this.scene.add(directionalLight);
  
    // Add orbit controls to allow user to rotate and zoom the camera
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
  
    // Set the camera position
    this.camera.position.set(0, 5, 10); // x, y, z coordinates
    this.controls.update();
  }

  // Adds the Eco-Bot model to the scene
  addEcoBot() {
    // ... (existing code for adding a simple box as a placeholder) ...

    // If importing a model, you would use a loader
    const loader = new GLTFLoader();
    loader.load('streamlit_app/assets/images/Eco_bot2.png.glb', (gltf) => {
      this.ecoBot = gltf.scene;
      this.scene.add(this.ecoBot);
      // Set the position and scale as needed
      this.ecoBot.position.set(0, 0, 0); // Adjust as necessary
      this.ecoBot.scale.set(1, 1, 1); // Adjust as necessary
    });
  }

  // Set up interactivity
  setupInteractivity() {
    this.renderer.domElement.addEventListener('click', (event) => {
      // Calculate mouse position in normalized device coordinates (-1 to +1) for both components
      const mouse = new THREE.Vector2();
      mouse.x = (event.clientX / this.renderer.domElement.clientWidth) * 2 - 1;
      mouse.y = - (event.clientY / this.renderer.domElement.clientHeight) * 2 + 1;
  
      // Update the picking ray with the camera and mouse position
      const raycaster = new THREE.Raycaster();
      raycaster.setFromCamera(mouse, this.camera);
  
      // Calculate objects intersecting the picking ray
      const intersects = raycaster.intersectObjects(this.scene.children);
  
      for (let i = 0; i < intersects.length; i++) {
        // Check if Eco-Bot is clicked and perform actions
        if (intersects[i].object === this.ecoBot) {
          console.log('Eco-Bot clicked');
          // Perform actions like displaying information or starting animations
        }
      }
    });
  }

  // Animation loop
  animate() {
    requestAnimationFrame(this.animate.bind(this)); // Bind the context to the class instance
    this.renderer.render(this.scene, this.camera);
    this.controls.update();
  }
}

// Instantiate the conversation tree
const tree = new ConversationTree();



    

  