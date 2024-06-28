import { useState } from "react";
import React from "react";

function CustomForm() {
  // hook for capturing data from the form
  const [userInput, setUserInput] = useState({
    name: "",
    age: "",
    gender: "",
    question: "",
  });

  const [answer, setAnswer] = useState([]);

  const [isSubmitted, setIsSubmitted] = useState(false);

  //functions to transfer data from the form to the hook
  function handleNameChange(event) {
    setUserInput((uI) => ({ ...uI, name: event.target.value }));
  }

  function handleAgeChange(event) {
    setUserInput((uI) => ({ ...uI, age: event.target.value }));
  }

  function handleGenderChange(event) {
    setUserInput((uI) => ({ ...uI, gender: event.target.value }));
  }

  function handleQuestionChange(event) {
    setUserInput((uI) => ({ ...uI, question: event.target.value }));
  }

  //function to process the data from the form
  const handleSubmit = async (event) => {

    event.preventDefault();

    if (userInput.name === "" || userInput.age === "" || userInput.gender === "" || userInput.question === "") {
        alert('something is missing...');
        return;
    }

    setIsSubmitted(true);

    const res = await fetch(
      "http://localhost:5000/fortuneTelling?name=${userInput.name}&age=${userInput.age}&gender=${userInput.gender}&question=${userInput.question}",
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }
      }
    );

    if (res.ok) {
      const data = await res.json();
      setAnswer(data.answer);
    } else {
      console.error("Error:", res.statusText);
    }
  };

  return (
    <>
      {!isSubmitted && (
        <form id="form" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="name">
              <h1>What is your name?</h1>
            </label>
            <input
              type="text"
              id="name"
              placeholder="Yolanda"
              name="name"
              value={userInput.name}
              onChange={handleNameChange}
            />
          </div>
          <div>
            <label htmlFor="age">
              <h1>How old are you?</h1>
            </label>
            <input
              type="text"
              id="age"
              placeholder="30"
              value={userInput.age}
              onChange={handleAgeChange}
            />
          </div>
          <div>
            <label htmlFor="gender">
              <h1>Are you a man or a woman?</h1>
            </label>
            <select
              id="gender"
              value={userInput.gender}
              onChange={handleGenderChange}
              name="gender"
            >
              <option name="gender" value="male">
                Male
              </option>
              <option name="gender" value="female">
                Female
              </option>
            </select>
          </div>
          <div id="questions">
            <div>
              <h1>What is your question?</h1>
            </div>
            <div className="q">
              <input
                type="radio"
                id="future"
                name="questions"
                value="1"
                onClick={handleQuestionChange}
              />
              <label
                htmlFor="future"
                onClick={handleQuestionChange}
              >
                What does my career future hold?
              </label>
            </div>

            <div className="q">
              <input
                type="radio"
                id="love"
                name="questions"
                value="2"
                onClick={handleQuestionChange}
              />
              <label htmlFor="love" onClick={handleQuestionChange}>
                What does my love life look like?
              </label>
            </div>

            <div className="q">
              <input
                type="radio"
                id="finance"
                name="questions"
                value="3"
                onClick={handleQuestionChange}
              />
              <label htmlFor="finance" onClick={handleQuestionChange}>
                Will I be financially successful?
              </label>
            </div>

            <div className="q">
              <input
                type="radio"
                id="lifeChanges"
                name="questions"
                value="4"
                onClick={handleQuestionChange}
              />
              <label htmlFor="lifeChanges">
                What major life changes are coming my way?
              </label>
            </div>
          </div>
          <div>
            <button type="submit" id="submit">
              Magic
            </button>
          </div>
        </form>
      )}
      {answer ? (
        <p id="answer" className="answer">
          {answer}
        </p>
      ) : (
        <p>loading...</p>
      )}
    </>
  );
}

export default CustomForm;
