import React, { useState } from 'react';
import './index.css';

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

const PhilosophyHubTailwind = () => {
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
    <div className="min-h-screen bg-gray-50 text-gray-800 font-sans">
      {/* Header */}
      <header className="bg-gradient-to-tr from-blue-800 to-blue-600 text-white py-12 px-4 shadow-lg">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-4xl font-bold mb-2 drop-shadow-lg">PhilosophyHub</h1>
          <p className="text-lg opacity-90">Exploring the Spectrum of Human Thought</p>
        </div>
      </header>

      {/* Navigation */}
      <nav className="bg-white shadow-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 flex flex-wrap justify-center">
          <button
            onClick={() => setActiveTab('traditions')}
            className={`
              px-6 py-3 font-medium rounded-t-lg transition-all duration-200
              ${activeTab === 'traditions' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-500 hover:text-gray-700'}
            `}
          >
            Traditions
          </button>
          <button
            onClick={() => setActiveTab('timelines')}
            className={`
              px-6 py-3 font-medium rounded-t-lg transition-all duration-200
              ${activeTab === 'timelines' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-500 hover:text-gray-700'}
            `}
          >
            Timelines
          </button>
          <button
            onClick={() => setActiveTab('will-to-power')}
            className={`
              px-6 py-3 font-medium rounded-t-lg transition-all duration-200
              ${activeTab === 'will-to-power' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-500 hover:text-gray-700'}
            `}
          >
            Will-to-Power Spectrum
          </button>
          <button
            onClick={() => setActiveTab('search')}
            className={`
              px-6 py-3 font-medium rounded-t-lg transition-all duration-200
              ${activeTab === 'search' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-500 hover:text-gray-700'}
            `}
          >
            Search
          </button>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-8 px-4 flex-1">
        {/* Traditions Section */}
        {activeTab === 'traditions' && (
          <section className="mb-12">
            <h2 className="text-2xl font-bold text-blue-800 mb-6 flex items-center gap-3">
              Philosophical Traditions
            </h2>
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {filteredTraditions.map(tradition => (
                <div
                  key={tradition.id}
                  className="bg-white rounded-xl overflow-hidden shadow-lg transform transition-transform duration-300 hover:-translate-y-2 hover:shadow-xl"
                >
                  <div className="p-6">
                    <h3 className="text-xl font-semibold text-blue-800 mb-2">{tradition.name}</h3>
                    <p className="text-blue-600 italic mb-3">{tradition.period}</p>
                    <p className="text-gray-700 italic mb-4">{tradition.coreQuestion}</p>
                    <div className="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-500 mb-4">
                      <p className="font-medium text-gray-800">Unique Contribution:</p>
                      <p className="mt-1 text-gray-700">{tradition.uniqueContribution}</p>
                    </div>
                    <div className="mt-4">
                      <p className="font-medium text-gray-800 mb-2">Key Figures:</p>
                      <ul className="space-y-2">
                        {tradition.figures.map(figure => (
                          <li
                            key={figure.name}
                            className="border-t border-gray-200 py-2"
                          >
                            <div className="flex justify-between">
                              <span className="font-semibold">{figure.name}</span>
                              <span className="text-sm text-gray-600">({figure.period})</span>
                            </div>
                            <p className="mt-1 text-gray-700 text-sm">{figure.contribution}</p>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Timelines Section */}
        {activeTab === 'timelines' && (
          <section className="mb-12">
            <h2 className="text-2xl font-bold text-blue-800 mb-6 flex items-center gap-3">
              Chronological Timelines
            </h2>
            <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
              {traditionsData.map(tradition => (
                <div key={tradition.id} className="bg-white rounded-xl shadow-lg overflow-hidden">
                  <div className="bg-blue-800 text-white px-6 py-4">
                    <h3 className="text-lg font-semibold">{tradition.name} Timeline</h3>
                  </div>
                  <div className="p-6">
                    <div className="relative">
                      <div className="absolute inset-0 w-0.5 bg-gradient-to-t from-blue-500 to-red-500 left-1/2 transform -translate-x-1/2"></div>
                      {tradition.figures
                        .slice()
                        .sort((a, b) => {
                          const getYear = (periodStr) => {
                            const match = periodStr.match(/(\d{3,4})\s*[–-]/);
                            return match ? parseInt(match[1]) : 0;
                          };
                          return getYear(a.period) - getYear(b.period);
                        })
                        .map((figure, index) => (
                          <div
                            key={figure.name}
                            className={`
                              relative mb-8 w-[48%]
                              ${index % 2 === 0 ? 'left-0' : 'left-1/2'}
                            `}
                          >
                            <div className="absolute left-1/2 -translate-x-1/2 top-0 w-3 h-3 bg-blue-500 rounded-full ring-4 ring-blue-200"></div>
                            <div
                              className={`
                                absolute left-1/2 -translate-x-1/2 top-0
                                ${index % 2 === 0 ? '-translate-x-full translate-y-1/2' : 'translate-x-1/2 translate-y-1/2'}
                                bg-white p-4 rounded-lg shadow-lg w-[200px]
                              `}
                            >
                              <h4 className="text-lg font-semibold text-blue-800 mb-2">{figure.name}</h4>
                              <p className="text-blue-600 italic mb-2 text-sm">{figure.period}</p>
                              <p className="text-gray-700 text-sm">{figure.contribution}</p>
                            </div>
                          </div>
                        ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Will-to-Power Section */}
        {activeTab === 'will-to-power' && (
          <section className="mb-12 bg-gray-50 rounded-xl shadow-lg overflow-hidden">
            <div className="p-8">
              <h2 className="text-2xl font-bold text-blue-800 mb-6 flex items-center gap-3">
                Will-to-Power Spectrum
              </h2>
              <p className="text-gray-700 mb-6 leading-relaxed">
                Visualization of philosophies ranked by their will-to-power score (-100 to +100)
              </p>
              <div className="space-y-6">
                {willToPowerData.map((category, index) => (
                  <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden">
                    <div className="flex items-center justify-between px-6 py-4 bg-blue-500 text-white">
                      <span className="font-medium">{category.scoreRange}</span>
                      <span className="font-semibold">{category.label}</span>
                    </div>
                    <p className="px-6 py-2 text-gray-700">{category.description}</p>
                    <div className="px-6 py-4">
                      <p className="font-medium text-gray-800 mb-2">Representative Philosophies:</p>
                      <ul className="space-y-2">
                        {category.philosophies.map(philo => (
                          <li key={philo.name} className="border-t border-gray-200 py-2">
                            <div className="flex justify-between">
                              <span className="font-semibold">{philo.name}</span>
                              <span className="text-sm text-gray-600">{philo.contribution}</span>
                            </div>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                ))}
              </div>
              <div className="mt-8 pt-6 border-t border-gray-200 text-center text-gray-600 italic">
                <p>
                  <strong>Legend:</strong> -100 (Extinguishing will) → 0 (Neutral/Balanced) → +100 (Conquering will)
                </p>
              </div>
            </div>
          </section>
        )}

        {/* Search Section */}
        {activeTab === 'search' && (
          <section className="bg-white rounded-xl shadow-lg overflow-hidden">
            <div className="p-8">
              <h2 className="text-2xl font-bold text-blue-800 mb-6">Search Philosophies</h2>
              <form onSubmit={handleSearchSubmit} className="mb-6 flex gap-4">
                <input
                  type="text"
                  value={searchQuery}
                  onChange={handleSearchChange}
                  placeholder="Search traditions, figures, or concepts..."
                  className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-200 text-gray-800"
                />
                <button
                  type="submit"
                  className="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-all duration-200 shadow-lg"
                >
                  Search
                </button>
              </form>
              {searchQuery && (
                <div className="mt-8">
                  <h3 className="text-xl font-semibold text-blue-800 mb-4">Results for "{searchQuery}"</h3>
                  {filteredTraditions.length > 0 ? (
                    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
                      {filteredTraditions.map(tradition => (
                        <div
                          key={tradition.id}
                          className="bg-white rounded-xl overflow-hidden shadow-lg transform transition-transform duration-300 hover:-translate-y-2 hover:shadow-xl"
                        >
                          <div className="p-6">
                            <h3 className="text-xl font-semibold text-blue-800 mb-2">{tradition.name}</h3>
                            <p className="text-blue-600 italic mb-3">{tradition.period}</p>
                            <p className="text-gray-700 italic mb-4">{tradition.coreQuestion}</p>
                            <div className="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-500 mb-4">
                              <p className="font-medium text-gray-800">Unique Contribution:</p>
                              <p className="mt-1 text-gray-700">{tradition.uniqueContribution}</p>
                            </div>
                            <div className="mt-4">
                              <p className="font-medium text-gray-800 mb-2">Matching Figures:</p>
                              <ul className="space-y-2">
                                {tradition.figures
                                  .filter(figure =>
                                    figure.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                                    figure.contribution.toLowerCase().includes(searchQuery.toLowerCase())
                                  )
                                  .map(figure => (
                                    <li
                                      key={figure.name}
                                      className="border-t border-gray-200 py-2"
                                    >
                                      <div className="flex justify-between">
                                        <span className="font-semibold">{figure.name}</span>
                                        <span className="text-sm text-gray-600">({figure.period})</span>
                                      </div>
                                      <p className="mt-1 text-gray-700 text-sm">{figure.contribution}</p>
                                    </li>
                                  ))}
                              </ul>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <p className="text-gray-500 italic text-center py-8">No traditions match your search. Try different terms.</p>
                  )}
                </div>
              )}
            </div>
          </section>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-blue-800 text-white py-8 text-center text-sm">
        <p>PhilosophyHub &copy; 2026 | Explore the depth and breadth of human thought</p>
      </footer>
    </div>
  );
};

export default PhilosophyHubTailwind;