# Contributing — MindQuest

Panduan kerja tim untuk capstone DB11-G006.

## Branch Strategy

```
main         — production-ready code (protected, no direct commits)
dev          — integration branch (all features merged here first)
feature/*    — feature branches (cabang dari dev)
fix/*        — bug fixes
```

## Workflow Standar

1. **Pull latest dev**
   ```bash
   git checkout dev
   git pull origin dev
   ```

2. **Buat feature branch**
   ```bash
   git checkout -b feature/nama-fitur
   ```

3. **Commit dengan pesan jelas**
   ```bash
   git add .
   git commit -m "feat: tambah fitur leaderboard"
   ```

4. **Push dan buat Pull Request ke `dev`**
   ```bash
   git push origin feature/nama-fitur
   ```

5. **Tunggu review** dari minimal 1 anggota tim sebelum merge.

## Commit Message Convention

Gunakan prefix berikut:
- `feat:` — fitur baru
- `fix:` — bug fix
- `docs:` — perubahan dokumentasi
- `style:` — formatting, tidak ada perubahan logika
- `refactor:` — refactoring kode
- `test:` — penambahan/perubahan test
- `chore:` — maintenance, dependency, config

Contoh:
```
feat: tambah endpoint complete quest
fix: streak tidak reset saat skip 1 hari
docs: update README setup instructions
```

## Pembagian Tanggung Jawab

| Anggota | Area | Branch Prefix |
|---|---|---|
| Abiyyu Akmal | Frontend (UI, gamification state) | `feature/fe-abiyyu-*` |
| Fersdoven Josua | Frontend (API integration, deploy) | `feature/fe-fersdoven-*` |
| Syakha Hanan Abdillah | Backend (auth, models, quest API) | `feature/be-syakha-*` |
| Pendri Mikola | Backend (XP logic, streak, deploy) | `feature/be-pendri-*` |

## Daily Standup

Setiap pagi jam 09:00 WIB, semua anggota update:
- Apa yang dikerjakan kemarin
- Apa yang akan dikerjakan hari ini
- Ada blocker?

Update progress di Trello board sebelum standup.
