const pendingList = new Vue({
    el: '#pendingList',
    data: {},
    methods:{
        getPendingList(){
            var url = "http://127.0.0.1:8000/api/subject/pending_subject/"

            axios.get(url)
                .then(function (res) {
                    console.log(res)
                })

        }
    },
    beforeMount: function () {
        this.getPendingList()
    }

})