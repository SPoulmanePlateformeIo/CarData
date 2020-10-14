from app import server
import pandas as pd

df = pd.read_csv('data/carData.csv')
print(df)

app.layout = html.Div(('Hello Word!'))

if __name__ == '__main__':
    app.run_server(debug=True)
