today = () =>{
    document.getElementById('completedtasks').style.display="none";
    document.getElementById('alltasks').style.display="none";
    document.getElementById('tasks').style.display="block";
    document.getElementById('completed').style.fontWeight="normal";
    document.getElementById('all').style.fontWeight="normal";
    document.getElementById('today').style.fontWeight=600;
}
completedtasks = () =>{
    document.getElementById('tasks').style.display="none";
    document.getElementById('alltasks').style.display="none";
    document.getElementById('completedtasks').style.display="block";
    document.getElementById('today').style.fontWeight="normal";
    document.getElementById('all').style.fontWeight="normal";
    document.getElementById('completed').style.fontWeight=600;
}
allt = () =>{
    document.getElementById('tasks').style.display="none";
    document.getElementById('completedtasks').style.display="none";
    document.getElementById('alltasks').style.display="block";
    document.getElementById('today').style.fontWeight="normal";
    document.getElementById('completed').style.fontWeight='normal';
    document.getElementById('all').style.fontWeight=600;
    
}