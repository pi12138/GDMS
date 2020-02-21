var app = new Vue({
    el:"#app",
    data:{
        subjectName: "",
        teacher: "",
        office: "",
        number: "",
        student: "",
        subjectDesc:"",
        expectGoal: "",
        require: "",
        requiredConditions: "",
        references:""
    },
    methods:{
        showTable(){
            var div = document.getElementById('hidden_subject_table')
            var btn = document.getElementById('hidden_btn')
            div.classList.remove('hidden')
            btn.classList.remove('hidden')
        },

        hiddenTable(){
            var div = document.getElementById('hidden_subject_table')
            var btn = document.getElementById('hidden_btn')
            div.classList.add('hidden')
            btn.classList.add('hidden')
        },

        declareSubject(){
            var msg = this.verifyData()
            if (msg != true){
                alert(msg)
                return
            }

            var url = "http://127.0.0.1:8000/subject/declare_subject/"
            axios.post(url, this.$data)
                .then(function (res) {
                    alert(res.data)
                    window.location.href = '/subject/declare_subject/'
                })
                .catch(function (error) {
                    // console.log(error.response)
                    alert(error.response.data)
                })
        },

        getData(){
            this.teacher = document.getElementsByName('teacher-id')[0].value
            this.office = document.getElementsByName('office-id')[0].value
        },

        verifyData(){
            if (this.subjectName === ""){
                return "课题名为空"
            }

            if (this.number === ""){
                return "课题人数为空"
            }

            if (this.subjectDesc === ""){
                return "课题描述为空"
            }

            if (this.expectGoal === ""){
                return "预期目标为空"
            }

            if (this.require === ""){
                return "对学生知识能力要求为空"
            }

            if (this.requiredConditions === ""){
                return "所需条件为空"
            }

            if (this.references === ""){
                return "参考资料为空"
            }

            return true
        }
    },
    beforeMount(){
        this.getData()
    }
})


var subjectList = new Vue({
    el: "#subject_list",
    data: {},
    methods: {
        showSubjectInfo(subjectId){
            // console.log(subjectId)
            var url = "http://127.0.0.1:8000/subject/alter_subject/" + "?subject_id=" + subjectId

            axios.get(url)
                .then(function (res) {
                    if (res.status !== 200){
                        console.log(res)
                        return
                    }

                    var data = res.data
                    mark_form.subjectName = data.subject_name
                    mark_form.teacher = ""

                })
                .catch(function (error) {
                    console.log(error.response)
                })
        }
    }
})

var mark_form = new Vue({
    el: "#mark_form",
    data: {
        subjectName: "",
        teacher: "",
        office: "",
        number: "",
        student: "",
        subjectDesc:"",
        expectGoal: "",
        require: "",
        requiredConditions: "",
        references:""
    }
})