import React, { useState } from 'react';
import './PhilosophyHub.css';

const traditionsData = [
  {
    id: 1,
    name: 'Greek Philosophy',
    period: '6th Century BCE - 6th Century CE',
    coreQuestion: 'What is the nature of reality and the good life?',
    figures: [
      { name: 'Thales', period: 'c. 624–546 BCE', contribution: 'First philosopher; sought natural explanations' },
      { name: 'Socrates', period: '470–399 BCE', contribution: 'Socratic method; ethics-focused inquiry' },
      { name: 'Plato', period: '428–348 BCE', contribution: 'Theory of Forms; ideal state' },
      { name: 'Aristotle', period: '384–322 BCE', contribution: 'Logic, metaphysics, ethics, politics' },
      { name: 'Epicurus', period: '341–270 BCE', contribution: 'Atomism; pursuit of pleasure (ataraxia)' },
      { name: 'Zeno of Citium', period: '334–262 BCE', contribution: 'Founded Stoicism; virtue through reason' }
    ],
    uniqueContribution: 'Established Western philosophical inquiry and rational investigation of nature'
  },
  {
    id: 2,
    name: 'Indian Philosophy',
    period: '1500 BCE - Present',
    coreQuestion: 'What is the nature of self, reality, and liberation?',
    figures: [
      { name: 'Yajnavalkya', period: 'c. 8th Century BCE', contribution: 'Neti neti doctrine; self as pure consciousness' },
      { name: 'Buddha (Siddhartha Gautama)', period: 'c. 563–483 BCE', contribution: 'Four Noble Truths; Eightfold Path' },
      { name: 'Mahavira', period: '540–468 BCE', contribution: 'Jainism; ahimsa, karma, liberation' },
      { name: 'Adi Shankara', period: '788–820 CE', contribution: 'Advaita Vedanta; non-dualism of Brahman' },
      { name: 'Ramanuja', period: '1017–1137 CE', contribution: 'Vishishtadvaita; qualified non-dualism' },
      { name: 'Madhva', period: '1238–1317 CE', contribution: 'Dvaita Vedanta; strict dualism' }
    ],
    uniqueContribution: 'Developed sophisticated concepts of consciousness, karma, and liberation (moksha)'
  },
  {
    id: 3,
    name: 'Chinese Philosophy',
    period: '6th Century BCE - Present',
    coreQuestion: 'How should one live in harmony with the natural and social order?',
    figures: [
      { name: 'Confucius (Kongzi)', period: '551–479 BCE', contribution: 'Ren (benevolence), Li (ritual), social harmony' },
      { name: 'Laozi', period: '6th Century BCE', contribution: 'Dao De Jing; wu-wei, natural spontaneity' },
      { name: 'Mozi', period: '470–391 BCE', contribution: 'Universal love, utilitarianism, against aggression' },
      { name: 'Xunzi', period: '310–238 BCE', contribution: 'Confucian ritualism; human nature as evil' },
      { name: 'Zhuangzi', period: '369–286 BCE', contribution: 'Daoist relativism; freedom through spontaneity' },
      { name: 'Han Feizi', period: 'c. 280–233 BCE', contribution: 'Legalism; strict laws, state power' }
    ],
    uniqueContribution: 'Emphasized harmony, balance, and practical wisdom for social and natural order'
  },
  {
    id: 4,
    name: 'Islamic Philosophy',
    period: '8th Century CE - 14th Century CE',
    coreQuestion: 'How can reason and revelation be reconciled to understand God and creation?',
    figures: [
      { name: 'Al-Kindi', period: '801–873 CE', contribution: 'First Muslim peripatetic; synthesized Greek thought' },
      { name: 'Al-Farabi', period: '872–950 CE', contribution: 'Second Teacher; political philosophy, logic' },
      { name: 'Avicenna (Ibn Sina)', period: '980–1037 CE', contribution: 'Metaphysics, medicine, proof of God' },
      { name: 'Al-Ghazali', period: '1058–1111 CE', contribution: 'Critique of philosophy; revived Sufism' },
      { name: 'Averroes (Ibn Rushd)', period: '1126–1198 CE', contribution: 'Commentaries on Aristotle; reason and faith' },
      { name: 'Ibn Arabi', period: '1165–1240 CE', contribution: 'Sufi metaphysics; unity of being' }
    ],
    uniqueContribution: 'Preserved and expanded Greek philosophy while integrating Islamic theology'
  }
];

const willToPowerData = [
  {
    scoreRange: '-100 to -50',
    label: 'THE EXTINGUISHERS',
    description: 'Philosophies seeking annihilation, negation, or escape from existence',
    philosophies: [
      { name: 'Ajñana (Indian Materialism)', contribution: 'Radical skepticism; denial of knowledge possibility' },
      { name: 'Madhyamaka Buddhism (Nagarjuna)', contribution: 'Emptiness (shunyata); rejection of all views' },
      { name: 'Pyrrhonian Skepticism', contribution: 'Suspension of judgment; peace through non-assertion' },
      { name: 'Cārvāka (Lokayata)', contribution: 'Materialism; denial of afterlife, karma, gods' },
      { name: 'Epicureanism', contribution: 'Ataraxia through removal of fear and desire' },
      { name: 'Schopenhauer', contribution: 'Will as suffering; denial through asceticism' }
    ]
  },
  {
    scoreRange: '-45 to -10',
    label: 'THE SURRENDERERS',
    description: 'Philosophies of acceptance, resignation, or yielding to fate',
    philosophies: [
      { name: 'Stoicism (Epictetus, Marcus Aurelius)', contribution: 'Amor fati; acceptance of divine logos' },
      { name: 'Madhva Vedanta', contribution: 'Eternal damnation for some souls; acceptance of fate' },
      { name: 'Zoroastrian Zurvanism', contribution: 'Time as supreme; acceptance of cosmic order' },
      { name: 'Later School of Padmasambhava', contribution: 'Acceptance of hidden teachings (terma)' },
      { name: 'Quietism', contribution: 'Passive contemplation; surrender to divine will' },
      { name: 'Fatalism (Various traditions)', contribution: 'Events predetermined; resistance futile' }
    ]
  },
  {
    scoreRange: '-5 to +20',
    label: 'THE BALANCERS',
    description: 'Philosophies seeking equilibrium, moderation, and harmony',
    philosophies: [
      { name: 'Aristotelian Ethics', contribution: 'Golden mean; virtue as balance between extremes' },
      { name: 'Confucianism (Doctrine of the Mean)', contribution: 'Harmony through proper relationships' },
      { name: 'Theravada Buddhism', contribution: 'Middle way; balance between indulgence and asceticism' },
      { name: 'Classical Skepticism (Academic)', contribution: 'Probabilistic assent; suspension of dogmatism' },
      { name: 'Advaita Vedanta (Shankara)', contribution: 'Brahman as pure consciousness; world as appearance' },
      { name: 'Maimonides', contribution: 'Via negativa; balance through apophatic theology' }
    ]
  },
  {
    scoreRange: '+25 to +50',
    label: 'THE PRAGMATISTS',
    description: 'Philosophies focused on practical results, effectiveness, and worldly success',
    philosophies: [
      { name: 'Confucian Legalism (Han Feizi)', contribution: 'State power through law and technique' },
      { name: 'Mohist Utilitarianism', contribution: 'Maximize benefit; minimize harm through universal love' },
      { name: 'Lockean Empiricism', contribution: 'Knowledge from experience; practical politics' },
      { name: 'Utilitarianism (Bentham, Mill)', contribution: 'Greatest happiness for greatest number' },
      { name: 'Peircean Pragmatism', contribution: 'Truth as what works; fixation of belief' },
      { name: 'Wang Yangming', contribution: 'Unity of knowledge and action; innate moral knowledge' }
    ]
  },
  {
    scoreRange: '+55 to +80',
    label: 'THE WARRIORS',
    description: 'Philosophies of struggle, conquest, and asserting will over obstacles',
    philosophies: [
      { name: 'Nietzsche', contribution: 'Will to power; overcoming; Ubermensch as goal' },
      { name: 'Kshatriya Dharma', contribution: 'Warrior ethics; righteous battle as duty' },
      { name: 'Machievellian Realism', contribution: 'Power politics; ends justify means in statecraft' },
      { name: 'Samurai Bushido', contribution: 'Way of the warrior; loyalty, honor, martial mastery' },
      { name: 'Thrasymachean Sophism', contribution: 'Might makes right; justice as advantage of stronger' },
      { name: 'Social Darwinism', contribution: 'Survival of fittest applied to societies and races' }
    ]
  },
  {
    scoreRange: '+82 to +100',
    label: 'THE CONQUERORS',
    description: 'Philosophies of domination, transcendence, and imposing will on reality',
    philosophies: [
      { name: 'Fascist Ideologies', contribution: 'Total state control; struggle for national rebirth' },
      { name: 'Objectivism (Rand)', contribution: 'Rational egoism; laissez-faire capitalism; heroic individual' },
      { name: 'Tantrism (Left-Hand Path)', contribution: 'Transformation through taboo; kundalini awakening' },
      { name: 'Leninist Vanguardism', contribution: 'Dictatorship of proletariat; revolutionary party' },
      { name: 'Thelema (Crowley)', contribution: 'Do what thou wilt; love is the law, love under will' },
      { name: 'Transhumanism', contribution: 'Use technology to transcend human limitations' }
    ]
  }
];

const PhilosophyHub = () => {
  const [activeTab, setActiveTab] = useState('traditions');
  const [searchQuery, setSearchQuery] = useState('');
  const [filteredTraditions, setFilteredTraditions] = useState(traditionsData);

  // Filter traditions based on search query
  const filterTraditions = () => {
    if (!searchQuery.trim()) {
      setFilteredTraditions(traditionsData);
      return;
    }

    const query = searchQuery.toLowerCase().trim();
    const filtered = traditionsData.filter(tradition =>
      tradition.name.toLowerCase().includes(query) ||
      tradition.coreQuestion.toLowerCase().includes(query) ||
      tradition.figures.some(figure =>
        figure.name.toLowerCase().includes(query) ||
        figure.contribution.toLowerCase().includes(query)
      )
    );
    setFilteredTraditions(filtered);
  };

  // Handle search input change
  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  // Handle search submission
  const handleSearchSubmit = (e) => {
    e.preventDefault();
    filterTraditions();
  };

  return (
    <div className="philosophy-hub">
      <header className="app-header">
        <h1>PhilosophyHub</h1>
        <p>Exploring the Spectrum of Human Thought</p>
      </header>

      <nav className="tab-nav">
        <button
          className={activeTab === 'traditions' ? 'tab-active' : 'tab-inactive'}
          onClick={() => setActiveTab('traditions')}
        >
          Traditions
        </button>
        <button
          className={activeTab === 'timelines' ? 'tab-active' : 'tab-inactive'}
          onClick={() => setActiveTab('timelines')}
        >
          Timelines
        </button>
        <button
          className={activeTab === 'will-to-power' ? 'tab-active' : 'tab-inactive'}
          onClick={() => setActiveTab('will-to-power')}
        >
          Will-to-Power Spectrum
        </button>
        <button
          className={activeTab === 'search' ? 'tab-active' : 'tab-inactive'}
          onClick={() => setActiveTab('search')}
        >
          Search
        </button>
      </nav>

      <main className="app-main">
        {activeTab === 'traditions' && (
          <section className="traditions-section">
            <h2>Philosophical Traditions</h2>
            <div className="traditions-grid">
              {filteredTraditions.map(tradition => (
                <div key={tradition.id} className="tradition-card">
                  <h3>{tradition.name}</h3>
                  <p className="period">{tradition.period}</p>
                  <p className="core-question">{tradition.coreQuestion}</p>
                  <div className="unique-contribution">
                    <strong>Unique Contribution:</strong> {tradition.uniqueContribution}
                  </div>
                  <div className="figures">
                    <strong>Key Figures:</strong>
                    <ul>
                      {tradition.figures.map(figure => (
                        <li key={figure.name}>
                          <strong>{figure.name}</strong> ({figure.period}): {figure.contribution}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {activeTab === 'timelines' && (
          <section className="timelines-section">
            <h2>Chronological Timelines</h2>
            <div className="timelines-container">
              {traditionsData.map(tradition => (
                <div key={tradition.id} className="timeline-block">
                  <h3>{tradition.name} Timeline</h3>
                  <div className="timeline">
                    {/* Sort figures by approximate date for timeline positioning */}
                    {tradition.figures
                      .slice()
                      .sort((a, b) => {
                        // Extract years from period strings (simplified)
                        const getYear = (periodStr) => {
                          const match = periodStr.match(/(\d{3,4})\s*[–-]/);
                          return match ? parseInt(match[1]) : 0;
                        };
                        return getYear(a.period) - getYear(b.period);
                      })
                      .map((figure, index) => (
                        <div key={figure.name} className="timeline-item">
                          <div className="timeline-dot"></div>
                          <div className="timeline-content">
                            <h4>{figure.name}</h4>
                            <p className="figure-period">{figure.period}</p>
                            <p>{figure.contribution}</p>
                          </div>
                        </div>
                      ))}
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {activeTab === 'will-to-power' && (
          <section className="will-to-power-section">
            <h2>Will-to-Power Spectrum</h2>
            <p className="spectrum-description">
              Visualization of philosophies ranked by their will-to-power score (-100 to +100)
            </p>
            <div className="spectrum-container">
              {willToPowerData.map((category, index) => (
                <div key={index} className="spectrum-category">
                  <div className="category-header">
                    <span className="score-range">{category.scoreRange}</span>
                    <span className="category-label">{category.label}</span>
                  </div>
                  <p className="category-description">{category.description}</p>
                  <div className="philosophies-list">
                    <strong>Representative Philosophies:</strong>
                    <ul>
                      {category.philosophies.map(philo => (
                        <li key={philo.name}>
                          <strong>{philo.name}</strong>: {philo.contribution}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
            <div className="spectrum-legend">
              <p>
                <strong>Legend:</strong> -100 (Extinguishing will) → 0 (Neutral/Balanced) → +100 (Conquering will)
              </p>
            </div>
          </section>
        )}

        {activeTab === 'search' && (
          <section className="search-section">
            <h2>Search Philosophies</h2>
            <form onSubmit={handleSearchSubmit} className="search-form">
              <input
                type="text"
                value={searchQuery}
                onChange={handleSearchChange}
                placeholder="Search traditions, figures, or concepts..."
                className="search-input"
              />
              <button type="submit" className="search-button">
                Search
              </button>
            </form>
            {searchQuery && (
              <div className="search-results">
                <h3>Results for "{searchQuery}"</h3>
                {filteredTraditions.length > 0 ? (
                  <div className="traditions-grid">
                    {filteredTraditions.map(tradition => (
                      <div key={tradition.id} className="tradition-card">
                        <h3>{tradition.name}</h3>
                        <p className="period">{tradition.period}</p>
                        <p className="core-question">{tradition.coreQuestion}</p>
                        <div className="unique-contribution">
                          <strong>Unique Contribution:</strong> {tradition.uniqueContribution}
                        </div>
                        <div className="figures">
                          <strong>Matching Figures:</strong>
                          <ul>
                            {tradition.figures
                              .filter(figure =>
                                figure.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                                figure.contribution.toLowerCase().includes(searchQuery.toLowerCase())
                              )
                              .map(figure => (
                                <li key={figure.name}>
                                  <strong>{figure.name}</strong> ({figure.period}): {figure.contribution}
                                </li>
                              ))}
                          </ul>
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="no-results">No traditions match your search. Try different terms.</p>
                )}
              </div>
            )}
          </section>
        )}
      </main>

      <footer className="app-footer">
        <p>PhilosophyHub &copy; 2026 | Explore the depth and breadth of human thought</p>
      </footer>
    </div>
  );
};

export default PhilosophyHub;