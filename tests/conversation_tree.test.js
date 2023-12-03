// Import the necessary dependencies
const THREE = require('three');
const { createTree } = require('../gbts/visualizations/conversation_tree');

// Mock the scene object
const scene = new THREE.Scene();

// Test the createTree function
describe('createTree', () => {
  beforeEach(() => {
    // Clear the scene before each test
    scene.clear();
  });

  test('should add trunk, branches, and leaves to the scene', () => {
    // Call the createTree function
    createTree(scene);

    // Assert that the trunk, branches, and leaves are added to the scene
    expect(scene.children.length).toBe(5);
  });

  test('should set the correct positions for the branches and leaves', () => {
    // Call the createTree function
    createTree(scene);

    // Assert that the positions of the branches and leaves are set correctly
    expect(scene.children[1].position).toEqual(new THREE.Vector3(2, 5, 0));
    expect(scene.children[2].position).toEqual(new THREE.Vector3(-2, 5, 0));
    expect(scene.children[3].position).toEqual(new THREE.Vector3(2, 8, 0));
    expect(scene.children[4].position).toEqual(new THREE.Vector3(-2, 8, 0));
  });
});