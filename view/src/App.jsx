import { useState, useEffect, useRef } from 'react'
import './App.css'

function App() {
  const [input, setInput] = useState('')
  const [encrypted, setEncrypted] = useState('')
  const [decrypted, setDecrypted] = useState('')
  const [loading, setLoading] = useState(false)
  const timerRef = useRef(null)

  useEffect(() => {
    if (timerRef.current) clearTimeout(timerRef.current)

    if (!input.trim()) return

    timerRef.current = setTimeout(async () => {
      setLoading(true)
      const body = { msg: input }
      try {
        const encRes = await fetch('/incript', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        })
        const encryptedText = await encRes.text()
        setEncrypted(encryptedText)

        const decRes = await fetch('/decript', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ msg: encryptedText }),
        })
        setDecrypted(await decRes.text())
      } catch {
        setEncrypted('Error')
        setDecrypted('Error')
      } finally {
        setLoading(false)
      }
    }, 300)

    return () => clearTimeout(timerRef.current)
  }, [input])

  return (
    <div className="card">
      <div className="input-group">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="input your message"
        />
      </div>
      <div className="feedback">
        <p className="encrypted">
          {input.trim()
            ? (encrypted || (loading ? '...' : ''))
            : 'incripted response'}
        </p>
        <p className="decrypted">
          {input.trim()
            ? (decrypted || (loading ? '...' : ''))
            : 'decripted response'}
        </p>
      </div>
    </div>
  )
}

export default App
