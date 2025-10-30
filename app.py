import streamlit as st
st.text("Hello, world!")
st.text("welcome to TKR")
st.text("Meerpet")
st.image("./images/1.jpg",width=300)
data= {
  "employees": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "age": 30,
      "skills": ["JavaScript", "HTML", "CSS"]
    },
    {
      "firstName": "Anna",
      "lastName": "Smith",
      "age": 25,

      "skills": ["Python", "SQL"]
    }
  ],
  "location": {
    "city": "New York",
    "country": "USA"
  }
}
st.dataframe(data)
st.json(data)
st.table(data)