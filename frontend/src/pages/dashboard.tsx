import { useState } from "react";

const Dashboard = () => {
    const [enteredLink, setEnteredLink] = useState('');
    return (
        <div>
            Dashboard
            <input  type="text"
            placeholder="Enter a link"
            value={enteredLink}/>
        </div>
    );
}

export default Dashboard;