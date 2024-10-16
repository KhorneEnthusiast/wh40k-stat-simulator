import logo from './logo.svg';
import './App.css';
import { useState } from 'react'; 





function MyButton() {
    const [buttonCounter, setButtonCounter] = useState(0);
    function incrementCounter() {
        setButtonCounter(buttonCounter + 1);
    }
    return (
        <button className="myButton" onClick={incrementCounter}>
            Button Count: {buttonCounter}
        </button>
    );
}
function StatsForm() {
    const handleInput = (event) => {
        // Use a regular expression to allow only numbers
        const value = event.target.value;
        const numericValue = value.replace(/[^0-9]/g, ''); // Replace non-numeric characters
        event.target.value = numericValue; // Update the input value
    }

    return (
        <div className="container">
            <div className="inputWrapper">
                <label>
                    Toughness:
                    <input
                        type="text"
                        name="toughnessInput"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput}
                    />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    # of Attacks:
                    <input
                        type="text"
                        name="attacksInput"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    Weapon Strength:
                    <input
                        type="text"
                        name="wepStrInput"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    Armor Save:
                    <input
                        type="text"
                        name="armorSaveInput"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    Wounds:
                    <input
                        type="text"
                        name="woundsInput"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
        </div>
    );
}

function StatsForm2() {
    const handleInput = (event) => {
        // Use a regular expression to allow only numbers
        const value = event.target.value;
        const numericValue = value.replace(/[^0-9]/g, ''); // Replace non-numeric characters
        event.target.value = numericValue; // Update the input value
    }

    return (
        <div className="container">
            <div className="inputWrapper">
                <label>
                    Toughness:
                    <input
                        type="text"
                        name="toughnessInput2"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput}
                    />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    # of Attacks:
                    <input
                        type="text"
                        name="attacksInput2"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    Weapon Strength:
                    <input
                        type="text"
                        name="wepStrInput2"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    Armor Save:
                    <input
                        type="text"
                        name="armorSaveInput2"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
            <div className="inputWrapper">
                <label>
                    Wounds:
                    <input
                        type="text"
                        name="woundsInput2"
                        defaultValue="0"
                        className="statsInput"
                        onInput={handleInput} />
                </label>
            </div>
        </div>
    );
}



function App() {
    return (
        <div className="App">
            <header className="App-header">
                <StatsForm />
                <StatsForm2 />
                <MyButton />
            </header>
        </div>
    );
}

export default App;
