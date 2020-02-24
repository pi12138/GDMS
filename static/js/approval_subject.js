const pendingList = new Vue({
    el: '#pendingList',
    data: {
        pendingList: [],
        count: "",
        nextUrl: "",
        previousUrl: "",
        numPages: "",
        page: ""
    },
    methods:{
        getPendingList(url){
            axios.get(url)
                .then((res) => {
                    console.log(res)
                    this.pendingList = res.data.results
                    this.count = res.data.count
                    this.nextUrl = res.data.next_url
                    this.previousUrl = res.data.previous_url
                    this.numPages = res.data.num_pages
                    this.page = res.data.page
                    this.setBtnDisable()
                })
                .catch(function (error) {
                    console.log(error)
                    console.log(error.response)
                    alert("Error")
                })
        },
        getSubjectInfo(index){
            const subject = this.pendingList[index]
            markForm.setFormShow(subject)
        },

        setBtnDisable(){
            if (this.nextUrl == null){
                this.$refs.nextBtn.classList.add('disabled')
            }else{
                this.$refs.nextBtn.classList.remove('disabled')
            }

            if (this.previousUrl == null){
                this.$refs.previousBtn.classList.add('disabled')
            }else{
                this.$refs.previousBtn.classList.remove('disabled')
            }
        }

    },
    beforeMount: function () {
        const url = "http://127.0.0.1:8000/api/subject/pending_subject/"
        this.getPendingList(url)
    }

});


const markForm = new Vue({
    el: "#markForm",
    data: {
        formData: "",
    },
    methods: {
        setFormShow(formData){
            console.log(formData)
            this.formData = formData
            this.$refs.markForm.classList.remove('hidden')
        }
    },

})