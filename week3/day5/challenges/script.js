// Initialize an empty array to hold the tasks
const tasks = [];

// Select DOM elements needed for interaction
const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const listTasks = document.querySelector('.listTasks');
const clearBtn = document.querySelector('.clear-btn');

// Adds a new task to the list
function addTask() {
    const taskText = taskInput.value.trim();
    
    // Prevent adding empty tasks
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }
    
    // Insert the new task object into the tasks array
    tasks.push({
        id: Date.now(),
        text: taskText,
        completed: false
    });
    
    // Refresh the task list display
    renderTasks();
    
    // Reset the input field for next task
    taskInput.value = '';
}

// Displays all tasks in the DOM
function renderTasks() {
    listTasks.innerHTML = '';
    
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

// Removes a task from the array by its id and updates the display
function deleteTask(taskId) {
    const taskIndex = tasks.findIndex(task => task.id === taskId);
    if (taskIndex > -1) {
        tasks.splice(taskIndex, 1);
        renderTasks();
    }
}

// Toggles the completion status of a task and re-renders the list
function toggleTask(taskId) {
    const task = tasks.find(task => task.id === taskId);
    if (task) {
        task.completed = !task.completed;
        renderTasks();
    }
}

// Remove only tasks that are marked as completed
function clearAllTasks() {
    // Keep only tasks that are not completed
    const activeTasks = tasks.filter(task => !task.completed);
    
    // Replace the tasks array content with active tasks
    tasks.length = 0;
    tasks.push(...activeTasks);
    
    // Update the UI
    renderTasks();
}

// Event handlers for form submission and buttons
taskForm.addEventListener('submit', function(e) {
    e.preventDefault();
    addTask();
});

clearBtn.addEventListener('click', clearAllTasks);

// Allow adding a task when pressing Enter key inside the input
taskInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        addTask();
    }
});
