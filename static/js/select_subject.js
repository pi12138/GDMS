/* 学生模块: 选择课题 */

var subjectList = new Vue({
    el: "#subjectList",
    data: {
        formData: "",
        tableData: "",
        subjectName: "",
        office: 0,
        questioner: "",
        next_url: "",
        previous_url: "",
        count: "",
        num_pages: "",
        page: ""
    },
    methods: {
        getSubjectList(url){
            /* 获取课题列表 */

            const params = {
                subject_name: this.subjectName,
                office: this.office,
                questioner: this.questioner
            }

            axios.get(url, {params: params})
                .then(res => {
                    console.log(res)
                    this.tableData = res.data.results
                })
                .catch(error => {
                    console.log(error)
                    console.log(error.response)
                    alert("Error")
                })
        }

    },

    beforeMount(){
        const url = 'http://127.0.0.1:8000/api/subject/select_subject/'
        this.getSubjectList(url)
    }

})


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