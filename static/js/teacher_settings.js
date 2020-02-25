const teacherInfo = new Vue({
    el: '#teacherInfo',
    data: {
        formData: "",
        officeList: "",
    },
    methods: {
        getFormData(){
            const url = 'http://127.0.0.1:8000/api/user/teacher_settings/'

            axios.get(url)
                .then(res => {
                    console.log(res)
                    this.formData = res.data

                    this.getOfficeList(res.data.faculty)
                })
                .catch(error => {
                    console.log(error)
                    console.log(error.response)
                    alert("Error")
                })
        },

        getOfficeList(faculty){
            const url = 'http://127.0.0.1:8000/organization/offices/?faculty=' + faculty

            axios.get(url)
                .then(res => {
                    console.log(res)
                    this.officeList = res.data
                })
                .catch(error => {
                    console.log(error)
                    console.log(error.response)
                    alert("Error")
                })
        }
    },

    beforeMount(){
        this.getFormData()
    }
})