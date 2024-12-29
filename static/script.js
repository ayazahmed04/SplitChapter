const dropArea = document.getElementById('drop-area')
const fileInput = document.getElementById('file-input')
const uploadForm = document.getElementById('upload-form')
const uploadBtn = document.getElementById('upload-btn')

// Highlight drop area when file is dragged over
;['dragenter', 'dragover'].forEach((event) => {
   dropArea.addEventListener(event, (e) => {
      e.preventDefault()
      dropArea.classList.add('drag-over')
   })
})

// Remove highlight when file is dragged out or dropped
;['dragleave', 'drop'].forEach((event) => {
   dropArea.addEventListener(event, (e) => {
      e.preventDefault()
      dropArea.classList.remove('drag-over')
   })
})

// Handle dropped files
dropArea.addEventListener('drop', (e) => {
   e.preventDefault()
   const files = e.dataTransfer.files
   if (files.length) {
      fileInput.files = files // Attach the dropped files to the hidden file input
      uploadForm.submit() // Automatically submit the form
   }
})

// Trigger file input click on button click
uploadBtn.addEventListener('click', () => fileInput.click())
