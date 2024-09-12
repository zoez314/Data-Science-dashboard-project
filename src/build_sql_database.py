from utils import *
import pandas as pd
from sqlite3 import connect



flatfile = project_root / 'src' / 'data' / 'employee_events.csv'
db_path = package_path / 'employee_events.db'

print(db_path)



df = pd.read_csv(flatfile, encoding='cp1252')

table_settings = {
    'employee': {
        'column_map': {
            'sub_ID': 'employee_id',
            'sub_fname': 'first_name',
            'sub_lname': 'last_name',
            'sub_age': 'age',
            'sub_sex': 'sex'
            },
        'unique_id': ['employee_id'],
        },
    'team': {
        'column_map': {
            'sub_shift': 'shift_name',
            'sub_team': 'team_name',
            },
        'unique_id': ['team_name'],
        },
    'employee_events': {
        'column_map': {
            'record_comptype': 'event_type',
            'sub_team': 'team_name',
            'sub_ID': 'employee_id',
            'sup_ID': 'manager_id',
            'event_date': 'event_date'
            },
        },
    'manager_notes': {
        'column_map' :  {
            'recorded_note_from_sup': 'note',
            'event_date': 'note_date',
            'sup_ID': 'manager_id',
            'sub_ID': 'employee_id',
            'sub_team': 'team_name',
            },
        'drop_id': 'note'
        },
    'manager': {
        'column_map': {
            'sup_ID': 'manager_id',
            'sup_fname': 'first_name',
            'sup_lname': 'last_name',
            'sup_age': 'age',
            'sup_sex': 'sex',
            },
        'unique_id': ['manager_id']
        }
}


tables = {}
for table_name, settings in table_settings.items():
    frame = df.rename(columns=settings['column_map'])
    if unique_id := settings.get('unique_id'):
        frame = frame.drop_duplicates(subset=unique_id)
    if drop_id := settings.get('drop_id'):
        frame = frame[(frame[drop_id] != 'None') & (~frame[drop_id].isna())]
    
    tables[table_name] = frame[settings['column_map'].values()]

tables['team']['team_id'] = tables['team']['team_name'].str.split().apply(lambda x: x[-1])
tables['manager_notes'] = tables['manager_notes'].merge(tables['team'], on='team_name')[tables['manager_notes'].columns.tolist() + ['team_id']]
tables['manager'] = tables['manager'].assign(
    full_name = lambda x: x.first_name + ' ' + x.last_name,
    ).drop(['first_name', 'last_name'], axis=1)



event_type_map = {
    'Presence': 'Positive',
    'Efficacy': None,
    'Feat': 'Positive',
    'Slip': 'Negative',
    'Sacrifice': 'Positive',
    'Lapse': 'Negative',
    'Idea': 'Positive',
    'Teamwork': 'Positive',
    'Absence': 'Negative',
    'Disruption': 'Negative',
    'None': None,
    'Resignation': None,
    'Termination': None,
    'Onboarding': None,
    'Sabotage': 'Negative'
    }


team_map = {}
tables['team'].apply(lambda x: team_map.update({x.team_name: x.team_id}), axis=1)
print(team_map)


tables['employee_events'] = tables['employee_events'].assign(
    event_type=lambda x: x.event_type.map(event_type_map),
    event_date=lambda x: pd.to_datetime(x.event_date),
    team_id=lambda x: x.team_name.map(team_map),
    ).dropna(subset=['event_type'])

connection = connect(db_path.as_posix())

for table_name, table in tables.items():

    table.to_sql(table_name, connection, index=False, if_exists='replace')

connection.close()