/* 通用功能：
 * 学生： 上传毕业设计 + 下载毕业设计
 * 教师： 下载毕业设计 + 审阅毕业设计
 * 管理员： 下载毕业设计 + 查看毕业设计结果
 * */

const designForm = new Vue({
    el: "#designForm",
    data: {
        filename: "",
        fileSize: "",

        subjectName: "",
        subject: "",
        uploadTime: "",
        downloadFileUrl: "",
        design: "",
        reviewOption: "",
        reviewTime: "",

    },
    methods: {
        uploadFile(){
            /* 上传文件到 input[type="file"] */
            const uploadBtn = this.$refs.uploadFile
            uploadBtn.click()
        },

        getFileInfo(event){
            /* 获取一些文件信息 */
            const file = event.target.files[0]
            this.filename = file.name
            this.fileSize = file.size
        },

        showDesignForm(design, subjectName){
            if (design){
                this.getDesignData(design)
            }

            this.subjectName = subjectName
            this.$refs.designForm.classList.remove('hidden')
        },

        hiddenDesignForm(){
            this.$refs.designForm.classList.add('hidden')
        }
    },
    computed: {
        file: function(){
            return `文件名: ${this.filename}`
        }
    }
})