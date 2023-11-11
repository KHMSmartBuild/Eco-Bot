// Import Three.js and controls
import * as THREE from '../node_modules/three/build/three';
import { OrbitControls } from '../node_modules/three/examples/jsm/controls/OrbitControls';
// Setup the Three.js scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add orbit controls for camera manipulation
const controls = new OrbitControls(camera, renderer.domElement);
const container = document.getElementById('treeContainer');

// Adjust camera and renderer setup to use the container's dimensions
camera.aspect = container.clientWidth / container.clientHeight;
camera.updateProjectionMatrix();
renderer.setSize(container.clientWidth, container.clientHeight);
container.appendChild(renderer.domElement); // Append to the container instead of body

// Create your Three.js visual elements here (e.g., tree branches, leaves, etc.)
// ...
// Create your Three.js visual elements here (e.g., tree branches, leaves, etc.)
// Example: Create a tree with branches and leaves
const trunkGeometry = new THREE.CylinderGeometry(0.5, 0.5, 10);
const trunkMaterial = new THREE.MeshBasicMaterial({ color: 0x8B4513 });
const trunk = new THREE.Mesh(trunkGeometry, trunkMaterial);
scene.add(trunk);

const branchGeometry = new THREE.CylinderGeometry(0.2, 0.2, 5);
const branchMaterial = new THREE.MeshBasicMaterial({ color: 0x228B22 });
const branch1 = new THREE.Mesh(branchGeometry, branchMaterial);
branch1.position.set(0, 7, 0);
scene.add(branch1);

const branch2 = new THREE.Mesh(branchGeometry, branchMaterial);
branch2.position.set(0, 7, 2);
scene.add(branch2);

const leafGeometry = new THREE.SphereGeometry(1);
const leafMaterial = new THREE.MeshBasicMaterial({ color: 0x00FF00 });
const leaf1 = new THREE.Mesh(leafGeometry, leafMaterial);
leaf1.position.set(0, 10, 0);
scene.add(leaf1);

const leaf2 = new THREE.Mesh(leafGeometry, leafMaterial);
leaf2.position.set(0, 10, 2);
scene.add(leaf2);

// Animation loop for rendering the Three.js scene
function animate() {
    requestAnimationFrame(animate);
    controls.update(); // Only required if controls.enableDamping = true, or if controls.autoRotate = true
    renderer.render(scene, camera);
}
// Update resizing listener to adjust to the container's dimensions
window.addEventListener('resize', () => {
    camera.aspect = container.clientWidth / container.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
});

// Call the animate function to start the rendering loop
animate();

export { animate };