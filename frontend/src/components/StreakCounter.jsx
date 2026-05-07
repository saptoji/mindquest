import { Flame, Trophy } from 'lucide-react';

export default function StreakCounter({ current, best }) {
  return (
    <div className="card">
      <div className="grid grid-cols-2 gap-4">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <Flame className="w-4 h-4 text-orange-500" />
            <p className="text-xs text-slate-500">Streak saat ini</p>
          </div>
          <p className="text-2xl font-semibold text-slate-900">
            {current} <span className="text-sm text-slate-500 font-normal">hari</span>
          </p>
        </div>
        <div>
          <div className="flex items-center gap-2 mb-1">
            <Trophy className="w-4 h-4 text-amber-500" />
            <p className="text-xs text-slate-500">Streak terbaik</p>
          </div>
          <p className="text-2xl font-semibold text-slate-900">
            {best} <span className="text-sm text-slate-500 font-normal">hari</span>
          </p>
        </div>
      </div>
    </div>
  );
}
