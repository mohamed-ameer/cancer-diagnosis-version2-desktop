document.getElementById('dis').disabled = true;

let cancerTypeBtns = document.querySelectorAll('.cancer__type')
let bloodBtn = document.querySelector('.blood__btn')
let lungBtn = document.querySelector('.lung__btn')
let colonBtn = document.querySelector('.colon__btn')
let brainBtn = document.querySelector('.brain__btn')
let breastBtn = document.querySelector('.breast__btn')
let skinBtn = document.querySelector('.skin__btn')

const picture = document.getElementById('inputTag')

const formData = new FormData()

let data = {}

let queryS = ''
let file = ''


console.log(cancerTypeBtns);
function removeActiveClass(){
    for (var i = 0; i < cancerTypeBtns.length; i++) {
        cancerTypeBtns[i].classList.remove('active')
    }

}

bloodBtn.addEventListener('click', ()=>{
    removeActiveClass()
    bloodBtn.classList.add('active')
    queryS='blood'
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }
})
lungBtn.addEventListener('click', ()=>{
    removeActiveClass()
    lungBtn.classList.add('active')
    queryS='lung'
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }
})
colonBtn.addEventListener('click', ()=>{
    removeActiveClass()
    colonBtn.classList.add('active')
    queryS='colon'
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }
})
brainBtn.addEventListener('click', ()=>{
    removeActiveClass()
    brainBtn.classList.add('active')
    queryS='brain'
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }
})
breastBtn.addEventListener('click', ()=>{
    removeActiveClass()
    breastBtn.classList.add('active')
    queryS='breast'
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }
})
skinBtn.addEventListener('click', ()=>{
    removeActiveClass()
    skinBtn.classList.add('active')
    queryS='skin'
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }

})



function previewFile() {
    var preview = document.querySelector('.imgUpload');
    file = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "./assets/images/upload.svg";
    }
    if(queryS != '' && file ){
        document.getElementById('dis').disabled = false;
    }
    }


function sendData() {
    
    formData.append("picture", picture.files[0])
    console.log(formData);
    axios.post(`http://127.0.0.1:8000/api/cancerdetect/?type=${queryS}`, formData, {
        headers: {
        'Content-Type': formData.type
        }
    })
    .then(resp =>{
        data = resp.data
        setDataMero(data)
    })

    .catch(err => console.log(err));
}

function setDataMero(data){
    document.getElementById('cancer_type').innerText=data.cancer_type
    document.getElementById('explanation').innerText=data.explanation
    document.getElementById('recommendation').innerText=data.recommendation
    document.getElementById('dis').disabled = true;
    queryS = ''
}