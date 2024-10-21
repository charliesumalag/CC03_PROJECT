// BUTTONS
let addBtn = document.getElementById('add-btn');
let removeBtn = document.getElementById('remove-btn');
let viewBtn = document.getElementById('view-btn');
let updateBtn = document.getElementById('update-btn');

// FORMS
let addForm  = document.getElementById('add-form');
let udpateForm  = document.getElementById('update-form');
let removeForm  = document.getElementById('remove-form');
let viewField = document.getElementById('view-inventory');

let btnsAllEl = document.querySelectorAll('.btn');
let inputValEl = document.querySelectorAll('.input');

btnsAllEl.forEach((btn) => {

    document.getElementsByClassName('text').innerHTML = "Hello";
    // btn.addEventListener('click', () => {
    //     inputValEl.value = "";
    // })
})

// console.log(removeBtn);

removeBtn.addEventListener('click', () => {
    addBtn.classList.remove('btn-bg-color');
    updateBtn.classList.remove('btn-bg-color');
    removeBtn.classList.add('btn-bg-color');
    viewBtn.classList.remove('btn-bg-color');
    // console.log(updateBtn);

})

addBtn.addEventListener('click' , () => {
    addBtn.classList.add('btn-bg-color');
    updateBtn.classList.remove('btn-bg-color');
    removeBtn.classList.remove('btn-bg-color');
    viewBtn.classList.remove('btn-bg-color');

    addForm.classList.remove('display-none')
    removeForm.classList.add('display-none');
    udpateForm.classList.add('display-none');
    viewField.classList.add('display-none');
})
removeBtn.addEventListener('click' , () => {
    addBtn.classList.remove('btn-bg-color');
    updateBtn.classList.remove('btn-bg-color');
    removeBtn.classList.add('btn-bg-color');
    viewBtn.classList.remove('btn-bg-color');

    removeForm.classList.remove('display-none');
    addForm.classList.add('display-none');
    udpateForm.classList.add('display-none');
    viewField.classList.add('display-none');
});
updateBtn.addEventListener('click' , () => {
    addBtn.classList.remove('btn-bg-color');
    updateBtn.classList.add('btn-bg-color');
    removeBtn.classList.remove('btn-bg-color');
    viewBtn.classList.remove('btn-bg-color');


    udpateForm.classList.remove('display-none')
    addForm.classList.add('display-none');
    removeForm.classList.add('display-none');
    viewField.classList.add('display-none');
})
viewBtn.addEventListener('click' , () => {
    addBtn.classList.remove('btn-bg-color');
    updateBtn.classList.remove('btn-bg-color');
    removeBtn.classList.remove('btn-bg-color');
    viewBtn.classList.add('btn-bg-color');


    udpateForm.classList.add('display-none')
    addForm.classList.add('display-none');
    removeForm.classList.add('display-none');
    viewField.classList.remove('display-none');

})
console.log('hello');
