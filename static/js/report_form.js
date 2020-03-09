const reportForm = new Vue({
    el: "#reportForm",
    data: {
        subject: "",
        subjectName: "",
        submitTime: "",
        researchStatus: "",
        feasibilityAnalysis: "",
        problemsAndSolutions: "",
        workingConditions: "",
        programmeAndSchedule: "",
        guideTeacher: "",
        reviewOption: "",
        reviewTime: "",
        reviewResult: "",
        teacherName: ""
    },
    methods: {
        showReportForm(reportId, subjectName){
            /* 显示开题报告表单 */
            if (reportId){
                this.getReportData(reportId)
            }

            this.subjectName = subjectName
            this.$refs.reportForm.classList.remove('hidden')
        },

        getReportData(reportId){
            const url = 'http://127.0.0.1:8000/api/report/' + reportId + '/'

            axios.get(url)
                .then(res => {
                    const data = res.data.data
                    console.log(data)

                    this.subject = data.subject
                    this.subjectName = data.subject_name
                    this.submitTime = data.submit_time
                    this.researchStatus = data.research_status
                    this.feasibilityAnalysis = data.feasibility_analysis
                    this.problemsAndSolutions = data.problems_and_solutions
                    this.workingConditions = data.working_conditions
                    this.programmeAndSchedule = data.programme_and_schedule
                    this.guideTeacher = data.guide_teacher
                    this.reivewerOption = data.review_option
                    this.reviewTime = data.review_time
                    this.reviewResult = data.review_result
                })
                .catch(err => {
                    handleError(err)
                })
        },

        submitReportData(){
            const url = 'http://127.0.0.1:8000/api/report/'
            const csrfToken = getCookie('csrftoken')
            const headers = {
                'X-CSRFToken': csrfToken
            }
            const data = {
                research_status: this.researchStatus,
                feasibility_analysis: this.feasibilityAnalysis,
                problems_and_solutions: this.problemsAndSolutions,
                working_conditions: this.workingConditions,
                programme_and_schedule: this.programmeAndSchedule,
            }

            axios.post(url, data, {headers: headers})
                .then(res => {
                    console.log(res.data.data)
                    alert("提交成功")
                })
                .catch(err => {
                    handleError(err)
                })
        },

        hiddenReportForm(){
            this.$refs.reportForm.classList.add('hidden')
        }
    }
})


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