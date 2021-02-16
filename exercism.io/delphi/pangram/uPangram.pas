unit uPangram;

interface

function isPangram(aValue: string): boolean;

implementation

uses
  SysUtils, RegularExpressions;

function isPangram(aValue: string): boolean;
const
  alphabet = 'abcdefghijklmnopqrstvxwyz';
var
  regex: string;
begin
  if (aValue.IsEmpty) then
  begin
    Exit(false);
  end;
  regex := Format('[%s]', [aValue.ToLower]);
  Result := TRegex.Replace(alphabet, regex, '').IsEmpty;
end;

end.
