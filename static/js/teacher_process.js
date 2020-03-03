/* 教师功能: 毕业设计过程 */


const subjectList = new Vue({
    el: "#subjectList",
    data: {
        url: 'http://127.0.0.1:8000/api/subject/selected_subject/',
        subjectList: "",
        nextUrl: "",
        previousUrl: "",
        count:"",
        numPages: "",
        page: ""
    },
    methods: {
        getSubjectList(url){
            axios.get(url)
                .then(res => {
                    const data = res.data
                    console.log(data)

                    this.subjectList = data.results
                    this.nextUrl = data.next_url
                    this.previousUrl = data.previous_url
                    this.count = data.count
                    this.numPages = data.num_pages
                    this.page = data.page
                    this.setBtnDisable()
                })
                .catch(error => {

                })
        },

        setBtnDisable(){
            /* 设置按钮是否可以点击 */

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
        },

        handleTaskBook(taskId){
            /* 处理任务书字段 */

            if (taskId == null){
                return `<a href="#">填写</a>`
            }else{
                return `<a href="#">查看</a>`
            }
        },

        writeOrViewTaskBook(taskId){
            /* 填写课题任务书或者查看课题任务书 */

            if (taskId == null){
                console.log('填写')
            }else{
                console.log('查看')
            }
        }
    },

    beforeMount() {
        this.getSubjectList(this.url)
    }
})