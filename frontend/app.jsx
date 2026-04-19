const { useState, useEffect } = React;

const App = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        // Fetch schedule from production backend API
        fetch('https://gcp-conf-backend-bakadja-v2.onrender.com/api/schedule')
            .then(res => res.json())
            .then(json => {
                setData(json);
                setLoading(false);
            })
            .catch(err => {
                console.error("Error fetching data:", err);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div className="loading">Loading schedule...</div>;
    }

    if (!data) {
        return <div className="loading">Failed to load schedule. Ensure backend is running.</div>;
    }

    // Filter logic: Check title, category, or speaker names.
    const filteredEvents = data.events.filter(event => {
        if (!searchTerm) return true;
        const term = searchTerm.toLowerCase();
        
        const titleMatch = event.title.toLowerCase().includes(term);
        const categoryMatch = event.category.toLowerCase().includes(term);
        const speakerMatch = event.speakers.some(speaker => 
            `${speaker.firstName} ${speaker.lastName}`.toLowerCase().includes(term)
        );

        return titleMatch || categoryMatch || speakerMatch;
    });

    return (
        <div className="container">
            <header className="hero">
                <h1>{data.title}</h1>
                <div className="meta-info">
                    <span>📅 {data.date}</span>
                    <span>📍 {data.location}</span>
                </div>
            </header>

            <div className="search-container">
                <input 
                    type="text" 
                    className="search-input"
                    placeholder="Search by title, category, or speaker..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
            </div>

            <div className="schedule">
                {filteredEvents.length === 0 ? (
                    <div className="no-results">No events found matching "{searchTerm}"</div>
                ) : (
                    filteredEvents.map(event => (
                        <div key={event.id} className={`talk-card ${event.type === 'break' ? 'break-card' : ''}`}>
                            <div className="talk-header">
                                <span className="talk-time">{event.time}</span>
                                <span className="talk-category">{event.category}</span>
                            </div>
                            
                            <h2 className="talk-title">{event.title}</h2>
                            <p className="talk-description">{event.description}</p>
                            
                            {event.speakers.length > 0 && (
                                <div className="speakers">
                                    {event.speakers.map((speaker, idx) => (
                                        <div key={idx} className="speaker">
                                            <span>🗣️</span>
                                            <a href={speaker.linkedin} target="_blank" rel="noopener noreferrer">
                                                {speaker.firstName} {speaker.lastName}
                                            </a>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
