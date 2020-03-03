/* 教师功能: 毕业设计过程 */


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

        writeOrViewTaskBook(index){
            /* 填写课题任务书或者查看课题任务书 */
            const taskId = this.subjectList[index].task_book
            const subjectName = this.subjectList[index].subject_name
            const subjectId = this.subjectList[index].id
            taskBookForm.showTaskBook(taskId, subjectName, subjectId)
        },
    },

    beforeMount() {
        this.getSubjectList(this.url)
    }
})


const taskBookForm = new Vue({
    el: '#taskBookForm',
    data: {
        subject: "",
        releaseTime: "",
        subjectDesc: "",
        purposeAndSignificance: "",
        contentAndTechnology: "",
        dataAndInformation: "",
        schedule: "",
        references: "",
        informationInEnglish: "",
        reviewer: "",
        reviewTime: "",
        reviewResult: "",

        subjectName: "",
        reviewerName: ""

    },
    methods: {
        showTaskBook(taskId, subjectName, subjectId){
            /* 展示课题任务书 */

            if (taskId != null){
                this.getTaskBookData(taskId)
            }else{
                this.subjectName = subjectName
                this.subject = subjectId
            }

            this.$refs.taskBook.classList.remove('hidden')

            return true
        },

        hiddenTaskBook(){
            /* 隐藏课题任务书 */
            this.$refs.taskBook.classList.add('hidden')

            return true
        },

        getTaskBookData(taskId){
            /* 获取任务书数据 */
            const url = `http://127.0.0.1:8000/api/subject/task_book/${taskId}/`
            axios.get(url)
                .then(res => {
                    const data = res.data

                    this.subject = data.subject
                    this.releaseTime = data.releaseTime
                    this.subjectDesc = data.subject_desc
                    this.purposeAndSignificance = data.purpose_and_significance
                    this.contentAndTechnology = data.content_and_technology
                    this.dataAndInformation = data.data_and_information
                    this.schedule = data.schedule
                    this.references = data.references
                    this.informationInEnglish = data.information_in_English
                    this.reviewer = data.reviewer
                    this.reviewTime = data.review_time
                    this.reviewResult = data.review_result

                    this.subjectName = data.subjectName
                    this.reviewerName = data.reviewerName

                    return true
                })
                .catch(error => {
                    console.log(error)
                    console.log(error.response)
                    alert("Error")

                    return false
                })
        },

        submitTaskBookData(){
            /* 提交课题任务书 */

            const url = 'http://127.0.0.1:8000/api/subject/task_book/'
            const csrfToken = getCookie('csrftoken')
            const headers = {
                'X-CSRFToken': csrfToken
            }
            const data = {
                subject: this.subject,
                subject_desc: this.subjectDesc,
                purpose_and_significance: this.purposeAndSignificance,
                content_and_technology: this.contentAndTechnology,
                data_and_information: this.dataAndInformation,
                schedule: this.schedule,
                references: this.references,
                information_in_English: this.informationInEnglish,
            }

            axios.post(url, data, {headers: headers})
                .then(res => {
                    console.log(res.data)
                    alert("提交任务书成功")
                })
                .catch(err => {
                    console.log(err)
                    console.log(err.response)
                    alert("Error")
                    return false
                })
        }
    }
})