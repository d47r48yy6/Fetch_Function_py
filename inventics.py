import sqlite3

class ReportGenerator:
    def __init__(self, db_path='/Users/ayushyadav/inventics/sample.db/sample.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_call_statistics(self, month):
        query = f'''
            SELECT COUNT(call_id) AS total_calls, SUM(call_duration) AS total_duration
            FROM Calls
            WHERE strftime('%Y-%m', call_date) = '{month}'
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_message_statistics(self, month):
        query = f'''
            SELECT COUNT(message_id) AS total_messages
            FROM Messages
            WHERE strftime('%Y-%m', message_date) = '{month}'
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_direction_request_statistics(self, month):
        query = f'''
            SELECT COUNT(request_id) AS total_requests
            FROM PeopleAskedForDirection
            WHERE strftime('%Y-%m', request_date) = '{month}'
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_website_visits_statistics(self, month):
        query = f'''
            SELECT COUNT(visit_id) AS total_visits
            FROM WebsiteVisitsFromProfile
            WHERE strftime('%Y-%m', visit_date) = '{month}'
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_profile_view_statistics(self, month):
        query = f'''
            SELECT COUNT(view_id) AS total_views
            FROM ProfileViews
            WHERE strftime('%Y-%m', view_date) = '{month}'
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_search_statistics(self, month):
        query = f'''
            SELECT COUNT(search_id) AS total_searches
            FROM SearchesAppearance
            WHERE strftime('%Y-%m', search_date) = '{month}'
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def generate_monthly_report(self, month):
        report = {
            'Calls': self.get_call_statistics(month),
            'Messages': self.get_message_statistics(month),
            'DirectionRequests': self.get_direction_request_statistics(month),
            'WebsiteVisits': self.get_website_visits_statistics(month),
            'ProfileViews': self.get_profile_view_statistics(month),
            'Searches': self.get_search_statistics(month),
        }
        return report

def main():
    report_generator = ReportGenerator()


    month_report = report_generator.generate_monthly_report('2024-01')

    print("Monthly Report for January 2024:")
    for category, stats in month_report.items():
        print(f"{category} - {stats}")

if __name__ == "__main__":
    main()
