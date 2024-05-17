mytasks = () =>{
    document.getElementById('completedtasks').style.display="none";
    document.getElementById('tasks').style.display="block";
    document.getElementById('completed').style.fontWeight="normal";
    document.getElementById('mytasks').style.fontWeight=600;
}
completedtasks = () =>{
    document.getElementById('tasks').style.display="none";
    document.getElementById('completedtasks').style.display="block";
    document.getElementById('mytasks').style.fontWeight="normal";
    document.getElementById('completed').style.fontWeight=600;
}