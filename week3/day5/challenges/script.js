
const tasks = [];
const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const listTasks = document.querySelector('.listTasks');
const clearBtn = document.querySelector('.clear-btn');

// Function to add a task
function addTask() {
    const taskText = taskInput.value.trim();
    
    // Check that the input is not empty
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }
    
    // Add task to the array
    tasks.push({
        id: Date.now(),
        text: taskText,
        completed: false
    });
    
    // Add task to the DOM
    renderTasks();
    
    // Clear the input field
    taskInput.value = '';
}
// Function to render tasks
function renderTasks() {
    listTasks.innerHTML = '';
    // Loop through tasks and add them to the DOM
    tasks.forEach(task => {
        const taskItem = document.createElement('div');
        taskItem.className = 'task-item';
        
        taskItem.innerHTML = `
            <button class="delete-btn" onclick="deleteTask(${task.id})">
                <i class="fas fa-times"></i>
            </button>
            <input type="checkbox" class="task-checkbox" 
                   ${task.completed ? 'checked' : ''} 
                   onchange="toggleTask(${task.id})">
            <label class="task-label ${task.completed ? 'completed' : ''}">${task.text}</label>
        `;
        
        listTasks.appendChild(taskItem);
    });
}

// Function to delete a task
function deleteTask(taskId) {
    // Find the index of the task
    const taskIndex = tasks.findIndex(task => task.id === taskId);
    if (taskIndex > -1) {
        tasks.splice(taskIndex, 1);
        renderTasks();
    }
}

// Function to toggle task completion
function toggleTask(taskId) {
    // Find the task
    const task = tasks.find(task => task.id === taskId);
    if (task) {
        // Toggle the task completion
        task.completed = !task.completed;
        renderTasks();
    }
}

// Function to clear all tasks
function clearAllTasks() {
    tasks.length = 0;
    renderTasks();
}

// Event listeners
taskForm.addEventListener('submit', function(e) {
    e.preventDefault();
    addTask();
});
// Clear all tasks
clearBtn.addEventListener('click', clearAllTasks);

// Allow adding tasks by pressing Enter
taskInput.addEventListener('keypress', function(e) {
    // Check if the pressed key is Enter
    if (e.key === 'Enter') {
        // Prevent the default form submission
        e.preventDefault();
        // Add the task
        addTask();
    }
});