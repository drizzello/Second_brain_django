import {getCookie} from '../helpers/cookies'

export default class NotesApiCommon {
    
    static async getNotes() {
        const url = "http://localhost:8000/api/notes";
        try {
            const response = await fetch(url, {
            credentials: "include",
            });
            if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
            }

            return await response.json()
        } catch (error) {
            console.error(error.message);
        }
    }

    static async addNote(data) {
        const url = "http://localhost:8000/api/notes/add";
        const csrfToken = getCookie('csrftoken');
            try {
                const response = await fetch(url, {
                    credentials: "include",
                    headers: {
                        // 1. Specifichiamo che stiamo inviando un JSON
                        "Content-Type": "application/json",
                        // 2. Inseriamo il token CSRF che Django si aspetta
                        "X-CSRFToken": csrfToken || "",
                    },
                    method:"post",
                    body:JSON.stringify({
                        title: data.title,
                        content: data.content
                        }
                    ),
                }
                )

            return await response.json()
        } catch (error) {
            console.error(error.message);
        }
    }

    static async deleteNote(note_id) {
        const url = `http://localhost:8000/api/notes/delete/${note_id}`;
        const csrfToken = getCookie('csrftoken');
            try {
                const response = await fetch(url, {
                    credentials: "include",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken || "",
                    },
                    method:"delete",

                })

            return await response.json()
        } catch (error) {
            console.error(error.message);
        }
    }

    static async updateNote(note) {
        const url = `http://localhost:8000/api/notes/update/${note.id}`;
        const csrfToken = getCookie('csrftoken');
        try{
            const response = await fetch(url, {
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken || "",
                    },
                method:"put",
                body:JSON.stringify({
                    title: note.title,
                    content: note.content
                    }
                ),

                }
            )
        } catch (error){
            console.error(error);
        }
    }

}
