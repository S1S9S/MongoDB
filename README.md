# MongoDB
MongoDB usage example


1. Install MongoDB:
    brew tap mongodb/brew\n
    brew install mongodb-community@7.0

2. Start MongoDB:
    brew services start mongodb-community@7.0

3. Create new DataBase:
    use database (for creating new database, u can call db whatever u want, for example: use notesdb, name of ur db is notesdb)

4. Open IDE and install all requirements:
    pip insatll -r requirements.txt

5. Command for starting the project:
    uvicorn main:app --reload

