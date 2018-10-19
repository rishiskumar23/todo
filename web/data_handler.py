class DataManager(object):

    def __init__(self, queryset):
        self.queryset = queryset

    def get_data(self):
        data = []
        main_headers = ['To-do List', '', '', '', '', '', '', '']
        headers = []
        headers.append('Title')
        headers.append('Description')
        headers.append('Date')
        headers.append('Time')
        headers.append('Status')
        headers.append('Created Date')
        headers.append('Modified Date')
        headers.append('Is active')

        counter = 0
        res_data = []
        for response in self.queryset:
            counter += 1
            response_data = []
            response_data.append(response.title)
            response_data.append(response.description)
            response_data.append(response.date)
            response_data.append(response.time)
            response_data.append(response.get_status())
            response_data.append(response.created_date)
            response_data.append(response.modified_date)
            response_data.append(response.is_active)
            res_data.append(response_data)
        data.append(main_headers)
        data.append(headers)
        for d in res_data:
            data.append(d)
        return data
