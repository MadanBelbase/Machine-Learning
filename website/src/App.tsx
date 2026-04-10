import { useState, useEffect, useMemo } from 'react'
import './index.css'

interface Commit {
  sha: string;
  commit: {
    message: string;
    author: {
      date: string;
    };
  };
  html_url: string;
}

const GITHUB_REPO = "MadanBelbase/250-Day-ML";
const TOTAL_DAYS_GOAL = 250;

function App() {
  const [commits, setCommits] = useState<Commit[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Increase limit to 100 to show more activity
    fetch(`https://api.github.com/repos/${GITHUB_REPO}/commits?per_page=100`)
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data)) {
          setCommits(data);
        }
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching commits:", err);
        setLoading(false);
      });
  }, []);

  // Calculate activity for the heatmap
  const activityData = useMemo(() => {
    const counts: Record<string, number> = {};
    commits.forEach(c => {
      const date = new Date(c.commit.author.date).toISOString().split('T')[0];
      counts[date] = (counts[date] || 0) + 1;
    });
    return counts;
  }, [commits]);

  // Generate heatmap cells (last 6 months)
  const heatmapCells = useMemo(() => {
    const cells = [];
    const today = new Date();
    for (let i = 250; i >= 0; i--) {
      const d = new Date();
      d.setDate(today.getDate() - i);
      const dateStr = d.toISOString().split('T')[0];
      const count = activityData[dateStr] || 0;
      let level = 0;
      if (count > 0) level = 1;
      if (count > 2) level = 2;
      if (count > 5) level = 3;
      if (count > 10) level = 4;
      cells.push({ date: dateStr, level });
    }
    return cells;
  }, [activityData]);

  const daysCompleted = Object.keys(activityData).length;
  const progressPercent = Math.min((daysCompleted / TOTAL_DAYS_GOAL) * 100, 100);

  const milestones = [
    {
      title: "Phase 1: Foundations",
      description: "Python Basics, NumPy, Pandas, Matplotlib & Seaborn.",
      status: "Completed",
      date: "Day 1 - Day 13",
      icon: "🐍"
    },
    {
      title: "Phase 2: Machine Learning Basics",
      description: "Introduction to ML, Supervised Learning, Hyperparameter Tuning.",
      status: "In Progress",
      date: "Day 14 - Day 100",
      icon: "🤖"
    },
    {
      title: "Phase 3: Advanced ML & DL",
      description: "Neural Networks, Computer Vision, NLP.",
      status: "Upcoming",
      date: "Day 101 - Day 200",
      icon: "🧠"
    },
    {
      title: "Phase 4: Capstone & Portfolio",
      description: "Building end-to-end projects and deploying models.",
      status: "Upcoming",
      date: "Day 201 - Day 250",
      icon: "🚀"
    }
  ];

  return (
    <div className="app-container animate-fade-in">
      <header style={{ marginBottom: '4rem', textAlign: 'center' }}>
        <span className="badge">Tracking the Path</span>
        <h1><span className="gradient-text">250-Day ML Journey</span></h1>
        <div style={{ marginTop: '2rem', maxWidth: '600px', margin: '2rem auto' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem', fontSize: '0.9rem' }}>
            <span>Progress Tracking</span>
            <span>{daysCompleted} / {TOTAL_DAYS_GOAL} Days</span>
          </div>
          <div className="progress-container">
            <div className="progress-bar" style={{ width: `${progressPercent}%` }}></div>
          </div>
        </div>
      </header>

      <section className="stats-grid">
        <div className="glass-card stat-card">
          <span className="stat-value">{daysCompleted}</span>
          <span className="stat-label">Activity Days</span>
        </div>
        <div className="glass-card stat-card">
          <span className="stat-value">Phase 2</span>
          <span className="stat-label">Current Phase</span>
        </div>
        <div className="glass-card stat-card">
          <span className="stat-value">{commits.length}</span>
          <span className="stat-label">Total Commits</span>
        </div>
      </section>

      <section className="glass-card activity-section">
        <h3 style={{ marginBottom: '1.5rem' }}>Consistency Graph</h3>
        <div className="heatmap-container">
          <div className="heatmap-labels">
            <span>Sep</span><span>Oct</span><span>Nov</span><span>Dec</span><span>Jan</span><span>Feb</span><span>Mar</span>
          </div>
          <div className="heatmap-grid">
            {heatmapCells.map((cell, i) => (
              <div
                key={i}
                className="heatmap-cell"
                data-level={cell.level}
                title={`${cell.date}: ${cell.level === 0 ? 'No' : cell.level} contributions`}
              ></div>
            ))}
          </div>
        </div>
      </section>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '3rem', marginTop: '4rem' }}>
        <section>
          <h2>The Journey <span className="gradient-text">Timeline</span></h2>
          <div className="timeline">
            {milestones.map((m, i) => (
              <div key={i} className="timeline-item">
                <div className="timeline-dot"></div>
                <div className="timeline-content glass-card">
                  <span className="date">{m.date}</span>
                  <h3>{m.icon} {m.title}</h3>
                  <p>{m.description}</p>
                  <div style={{ marginTop: '1rem' }}>
                    <span className="status-badge" style={{
                      background: m.status === 'Completed' ? 'rgba(88, 166, 255, 0.1)' : m.status === 'In Progress' ? 'rgba(163, 113, 247, 0.1)' : 'rgba(139, 148, 158, 0.1)',
                      color: m.status === 'Completed' ? 'var(--accent-secondary)' : m.status === 'In Progress' ? 'var(--accent-primary)' : 'var(--text-secondary)',
                      borderColor: m.status === 'Completed' ? 'rgba(88, 166, 255, 0.2)' : m.status === 'In Progress' ? 'rgba(163, 113, 247, 0.2)' : 'rgba(139, 148, 158, 0.2)'
                    }}>
                      {m.status}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        <aside>
          <div className="glass-card">
            <h3 style={{ marginBottom: '1.5rem' }}>Commit History</h3>
            <div className="commit-feed-scroll">
              {loading ? (
                <p>Loading activity...</p>
              ) : (
                <div className="commit-list">
                  {commits.map((c) => (
                    <div key={c.sha} className="commit-item">
                      <div>
                        <a href={c.html_url} target="_blank" rel="noopener noreferrer" className="commit-msg" style={{ color: 'var(--accent-secondary)', textDecoration: 'none', fontSize: '0.9rem' }}>
                          {c.commit.message.split('\n')[0]}
                        </a>
                        <span className="commit-date">{new Date(c.commit.author.date).toLocaleDateString()}</span>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
            <a
              href={`https://github.com/${GITHUB_REPO}`}
              target="_blank"
              rel="noopener noreferrer"
              style={{ display: 'block', marginTop: '1.5rem', textAlign: 'center', color: 'var(--text-secondary)', textDecoration: 'none', fontSize: '0.8rem' }}
            >
              Full History on GitHub →
            </a>
          </div>

          <div className="glass-card" style={{ marginTop: '2rem' }}>
            <h3 style={{ marginBottom: '1rem' }}>Resources</h3>
            <ul style={{ listStyle: 'none', padding: 0 }}>
              <li style={{ marginBottom: '0.8rem' }}>
                <a href="#" style={{ color: 'var(--accent-secondary)', textDecoration: 'none', fontSize: '0.95rem' }}>📚 Reading List</a>
              </li>
              <li style={{ marginBottom: '0.8rem' }}>
                <a href="#" style={{ color: 'var(--accent-secondary)', textDecoration: 'none', fontSize: '0.95rem' }}>🛠️ Tools & Tech</a>
              </li>
              <li>
                <a href="#" style={{ color: 'var(--accent-secondary)', textDecoration: 'none', fontSize: '0.95rem' }}>📝 Study Notes</a>
              </li>
            </ul>
          </div>
        </aside>
      </div>

      <footer>
        <p>© {new Date().getFullYear()} Madan Belbase • 250-Day ML Journey • Built with React & Vite</p>
      </footer>
    </div>
  )
}

export default App
