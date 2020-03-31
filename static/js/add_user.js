/*
* 管理员功能： 添加系统用户
* */
function handleError(error){
    console.log(error)
    console.log(error.response)
    alert("Error")
}

function getCookie(name){
    /* 获取cookie中的csrftoken */
    var name = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++){
        var c = ca[i].trim();
        if (c.indexOf(name)==0) return c.substring(name.length,c.length);
    }
    return "";
}

function getHeaders() {
    /* 为获取post, put, patch请求获取headers*/
    let csrfToken = getCookie('csrftoken')
    let headers = {
        'X-CSRFToken': csrfToken
    }

    return headers
}


let addUser = new Vue({
    el: '#addUser',
    data: {},
    methods: {
        addAdminUser(){
            adminUser.showUserForm()
        },

        addStudentUser(){

        },

        addTeacherUser(){

        }
    }
})


let adminUser = new Vue({
    el: '#adminUser',
    data: {
        username: "",
        password: "",
        name: ""

    },
    methods: {
        createUser(){
            let url = '/api/user/'
            let headers = getHeaders()

            axios.post(url, this.$data, {headers: headers})
                .then(res => {
                    console.log(res.data)
                    alert('新建管理员用户成功')
                })
                .catch(err => {
                    handleError(err)
                })
        },

        showUserForm(){
            this.$refs.adminUser.classList.remove('hidden')
        },

        hiddenUserForm(){
            this.$refs.adminUser.classList.add('hidden')
        }
    }
});


let teacherUser = new Vue({
    el: '#teacherUser',
    data: {
        username: "",
        password: "",
        name: "",
        gender: "",
        education: "",
        teacher_title: "",
        phone: "",
        qq: '',
        office: ''
    },
    methods: {
        createUser(){
            let url = '/api/user/'
            let headers = getHeaders()

            axios.post(url, this.$data, {headers: headers})
                .then(res => {
                    console.log(res.data)
                    alert('创建教师用户成功')
                })
                .catch(err => {
                    handleError(err)
                })
        }
    }
})


let studentUser = new Vue({
    el: '#studentUser',
    data: {
        username: '',
        password: '',
        name: '',
        gender: '',
        klass: '',
        direction: '',
        profession: '',
        phone: '',
        qq: ''
    },
    methods: {
        createUser(){
            let url = '/api/user/'
            let headers = getHeaders()

            axios.post(url, this.$data, {headers: headers})
                .then(res => {
                    console.log(res.data)
                    alert('新建学生用户成功')
                })
                .catch(err => {
                    handleError(err)
                })
        }
    }
})