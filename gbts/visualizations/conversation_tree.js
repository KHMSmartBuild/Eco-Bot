// Import Three.js and controls
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@latest/build/three.module.js'
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@latest/examples/jsm/controls/OrbitControls.js';
document.addEventListener('DOMContentLoaded', (event) => {
// Get the container element
const container = document.getElementById('treeContainer');


// Setup the Three.js scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(container.clientWidth, container.clientHeight);
container.appendChild(renderer.domElement); // Append to the container instead of body

// Add orbit controls for camera manipulation
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
controls.dampingFactor = 0.25;

// Initialize the camera position
camera.position.z = 30;

// Add lights to the scene
const ambientLight = new THREE.AmbientLight(0x404040); // soft white light
scene.add(ambientLight);

// Function to create the tree elements
function createTree() {
    // Trunk
    const trunkGeometry = new THREE.CylinderGeometry(0.5, 0.5, 10);
    const trunkMaterial = new THREE.MeshStandardMaterial({ color: 0x8B4513 });
    const trunk = new THREE.Mesh(trunkGeometry, trunkMaterial);
    scene.add(trunk);

    // Branches
    const branchGeometry = new THREE.CylinderGeometry(0.1, 0.1, 5);
    const branchMaterial = new THREE.MeshStandardMaterial({ color: 0x228B22 });

    const branch1 = new THREE.Mesh(branchGeometry, branchMaterial);
    branch1.position.set(2, 5, 0);
    scene.add(branch1);

    const branch2 = new THREE.Mesh(branchGeometry, branchMaterial);
    branch2.position.set(-2, 5, 0);
    scene.add(branch2);

    // Leaves
    const leafGeometry = new THREE.SphereGeometry(0.5);
    const leafMaterial = new THREE.MeshStandardMaterial({ color: 0x00FF00 });

    const leaf1 = new THREE.Mesh(leafGeometry, leafMaterial);
    leaf1.position.set(2, 8, 0);
    scene.add(leaf1);

    const leaf2 = new THREE.Mesh(leafGeometry, leafMaterial);
    leaf2.position.set(-2, 8, 0);
    scene.add(leaf2);
}

// Call createTree to add the tree to the scene
createTree();

// Animation loop for rendering the Three.js scene
function animate() {
    console.log('Animating');
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
    onWindowResize(); // Call onWindowResize to update camera and renderer on window resize
}

// Resize Listener
function onWindowResize() {
    const aspectRatio = container.clientWidth > 0 ? container.clientWidth / container.clientHeight : 1;
    camera.aspect = aspectRatio;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
}

// Add the resize event listener
window.addEventListener('resize', onWindowResize, false);

// Start the animation loop
animate();
console.log('Done');

});
